import text2emotion as te
import speech_recognition as sr
import os
from datetime import datetime

# Firebase
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate(r"A:\MiniProjects_Vann\Ai_Diary\practice\serviceAccountKey.json")
 # Your downloaded JSON
firebase_admin.initialize_app(cred)
db = firestore.client()

# Speech recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak now:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        
        print("✅ You said:", text)
        emotion = te.get_emotion(text)

        print("😄 Detected emotions:", emotion)

        # Use timestamp for file + Firebase
        timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"entry_{timestamp_str}.txt"

        # Save to file
        with open(filename, "w") as f:
            f.write(text)
        print(f"📁 Saved as: {filename}")

        # Save to Firestore
        entry = {
            "text": text,
            "emotion": emotion,
            "timestamp": datetime.now()
        }

        db.collection("diary_entries").add(entry)
        print("✅ Entry saved to Firebase!")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("🚫 Could not request results from Google API")
