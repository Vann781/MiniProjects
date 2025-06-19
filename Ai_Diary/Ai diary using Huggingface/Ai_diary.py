#using transformers to detect the emotion of text 

from transformers import pipeline
import speech_recognition as sr
import os
from datetime import datetime

# Load emotion classifier pipeline
classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=True,
                      framework="pt")  # important to avoid tf

# Create notes folder if not exists
if not os.path.exists("notes"):
    os.makedirs("notes")

# Initialize speech recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak now...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("✅ You said:", text)

        # Classify emotion
        results = classifier(text)

        # Print results
        for result in results[0]:
            print(f"{result['label']}: {result['score']:.4f}")

        # Save entry
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"notes/entry_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write(f"Text: {text}\n")
            f.write("Emotions:\n")
            for result in results[0]:
                f.write(f"{result['label']}: {result['score']:.4f}\n")

        print(f"📁 Saved as: {filename}")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("🚫 Could not request results from Google API")
