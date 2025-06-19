# Using Transformers + Firebase to detect emotion of text and save in cloud

from transformers import pipeline
import speech_recognition as sr
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# -------- Initialize Firebase --------
# Load your service account JSON file here
cred = credentials.Certificate("A:\MiniProjects_Vann\hugging face\Aidiary_Sserviceaccount.json")
firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()

# -------- Load emotion classifier pipeline --------
classifier = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base", 
    return_all_scores=True,
    framework="pt"  # important to avoid tensorflow issues
)

# -------- Initialize speech recognizer --------
r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak now...")
    audio = r.listen(source)

    try:
        # -------- Convert speech to text --------
        text = r.recognize_google(audio)
        print("✅ You said:", text)

        # -------- Classify emotions from text --------
        results = classifier(text)

        # -------- Print emotions nicely --------
        print("\n🎭 Detected Emotions:")
        for result in results[0]:
            print(f"{result['label']}: {result['score']:.4f}")

        # -------- Prepare data for Firestore --------
        entry = {
            'text': text,
            'emotions': {result['label']: float(result['score']) for result in results[0]},
            'timestamp': datetime.utcnow()  # UTC timestamp
        }

        # -------- Save entry to Firestore --------
        db.collection('ai_diary_entries').add(entry)
        print("\n☁️ Saved entry to Firebase Firestore!")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("🚫 Could not request results from Google API")
