import text2emotion as te
import speech_recognition as sr
import os
from datetime import datetime


if not os.path.exists("notes"):
    os.makedirs("notes")

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak now:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        
        print("✅ You said:", text)
        emotion = te.get_emotion(text)

        print(emotion)

        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"notes/entry_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write(text)
        print(f"📁 Saved as: {filename}")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("🚫 Could not request results from Google API")
