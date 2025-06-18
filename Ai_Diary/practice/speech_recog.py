import speech_recognition as sr
import os
from datetime import datetime

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak now:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("✅ You said:", text)

        # Use timestamp as filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"entry_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write(text)
        print(f"📁 Saved as: {filename}")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("🚫 Could not request results from Google API")
