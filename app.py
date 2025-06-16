from flask import Flask, render_template, request, jsonify, send_from_directory
import whisper
import os
from datetime import datetime
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Load the Whisper model with Tamil language specified
model = whisper.load_model("turbo")

@app.route('/')
def index():
    return render_template('index_mic.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio data received'}), 400
    
    audio_file = request.files['audio_data']
    
    if audio_file:
        # Save the audio file with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording_{timestamp}.webm"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)
        
        try:
            # Transcribe with Tamil language forced
            result = model.transcribe(filepath, language="ta")
            
            # Filter out non-Tamil words using regex
            tamil_text = filter_tamil_only(result["text"])
            
            return jsonify({
                'transcription': tamil_text,
                'filename': filename
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

def filter_tamil_only(text):
    """Filter to keep only Tamil characters and spaces"""
    # Tamil Unicode range: U+0B80-U+0BFF
    # Also keep spaces, punctuation common in Tamil
    tamil_pattern = re.compile(
        r'[\u0B80-\u0BFF\u0B82\u0B83\u0BBE-\u0BCD\u0BD7\s]+'
    )
    
    # Find all Tamil sequences
    tamil_matches = tamil_pattern.finditer(text)
    
    # Combine valid sequences with single spaces
    filtered_text = ' '.join(match.group() for match in tamil_matches)
    
    # Clean up multiple spaces
    return ' '.join(filtered_text.split())

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)