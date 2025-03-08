# tests/test_mic.py
import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSpeak now (10-second window)...")
        audio = r.listen(source, timeout=10)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("API unavailable")

if __name__ == "__main__":
    test_microphone()