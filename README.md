# MiniProjects_Vann
📝 AI Voice Diary (with Emotion Detection)
This is a simple AI-powered Voice Diary app — where you can speak your diary entry → it converts speech to text → detects the emotion using HuggingFace transformers → and saves it in a "notes" folder as a text file.

🎁 Features
✅ Record voice → convert to text
✅ Detect emotion of your entry (joy, sadness, anger, etc.)
✅ Save the entry (text + emotion scores) in notes folder
✅ CLI based — no GUI required
✅ Uses HuggingFace transformer model (distilroberta-base)
✅ Fun mini project for AI & NLP learning 🚀

⚙️ Tech Stack
Python 3.10.x

Transformers (HuggingFace)

PyTorch

SpeechRecognition

PyAudio (for microphone input)


📂 Project Structure
AI_Diary/
├── hugging face/
│   └── face.py  # main script
├── notes/       # folder where entries are saved
└── README.md    # project info

🚀 How to Run

1️⃣ Clone repo:
git clone https://github.com/yourusername/MiniProjects_Vann.git
cd MiniProjects_Vann/AI_Diary/hugging face

2️⃣ Install requirements:
pip install transformers torch SpeechRecognition pyaudio

3️⃣ Run app:
python [file name].py

4️⃣ Speak...
✅ It will detect emotion and save entry as:
notes/entry_YYYY-MM-DD_HH-MM-SS.txt


💾 Example Output
🎙️ Speak now...
✅ You said: I am very happy today!

joy: 0.85
sadness: 0.02
anger: 0.01
...
📁 Saved as: notes/entry_2025-06-19_14-30-55.txt



📌 Notes
Model used: j-hartmann/emotion-english-distilroberta-base

You need microphone working

Python 3.10.x recommended

Tested on Windows 11 + Python 3.10

🙋‍♂️ About
Made by Vayu
B.Tech 2nd Year Student
Learning AI & NLP 🚀
