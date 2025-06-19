📝 AI Voice Diary — Emotion Detection using Transformers
This is a simple CLI-based AI diary app —
You can speak, and it will:

✅ Convert your voice to text
✅ Detect the emotion in your words using HuggingFace Transformers
✅ Save the entry to a timestamped .txt file inside a notes folder

🚀 Features
🎙️ Speech-to-Text using speech_recognition + Google Speech API

🤗 Emotion detection using distilroberta-base (by j-hartmann) on HuggingFace

🗂️ Automatically saves entries in notes/entry_TIMESTAMP.txt

CLI-based — simple to use — no GUI required!

🔥 Demo

$ python e.py
🎙️ Speak now...
✅ You said: Me Bhaiya bahut jyada Khush hun
anger: 0.0133
disgust: 0.0265
fear: 0.0178
joy: 0.0651
neutral: 0.8308
sadness: 0.0408
surprise: 0.0055
📁 Saved as: notes/entry_2025-06-19_14-35-55.txt
📦 Libraries used
Library	Version (tested)
transformers	4.36.x or 4.52.x
torch	2.7.x
speech_recognition	latest
pyaudio	latest
datetime, os	built-in Python

⚙️ Installation
1️⃣ Clone repo:

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2️⃣ Install dependencies:

pip install transformers torch speechrecognition pyaudio
🛠️ Notes
Works best with Python 3.9 or 3.10

In Python 3.11+, extra care needed with transformers versions

Needs working microphone

Needs Internet (Google Speech API)

🤝 Acknowledgements
HuggingFace j-hartmann/emotion-english-distilroberta-base

Google Speech Recognition API

Inspiration from AI Diaries & Journals

🔮 Future Improvements
Add GUI using tkinter or streamlit

Save entries to Firebase

Display emotion graph

Detect emotion from images (OpenCV + FER)
