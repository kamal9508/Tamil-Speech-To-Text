# 🗣️ Tamil Speech-to-Text Web Application

This is a web-based application for converting **Tamil speech into text**. Users can either **record live audio** or **upload audio files**, and receive **real-time transcription in Tamil**. This tool is built using **Python Flask**, with HTML5 microphone integration and speech processing logic running in the backend.

---

## 🔥 Key Features

- 🎙️ **Live recording** directly from the browser
- 📂 Upload support for `.webm` and `.mp3` files
- 📝 Real-time **Tamil transcription**
- 🔊 Playback feature for recorded audio
- 🌐 Accessible via web (ngrok or local hosting)

---

## 📸 Project Demo

Below is a screenshot of the transcription output from the live web application:

![Sample Tamil Transcription Output](ee3bb28d-84ac-416b-8451-b4ccd0434e56.png)

*Fig A.3 - Sample transcription using the website*

---

## 📁 Folder Structure

Project/
│
├── app.py # Main Flask server script
├── templates/
│ └── index_mic.html # Webpage UI for audio recording
├── testing/
│ ├── audio_1.mp3 # Sample audio inputs
│ └── code.ipynb # Notebook for model/testing
├── uploads/ # Stores uploaded or recorded user audio files



