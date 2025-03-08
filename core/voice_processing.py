import speech_recognition as sr
import pyttsx3

class VoiceEngine:

    def list_voices(self):
        voices = self.engine.getProperty('voices')
        for index, voice in enumerate(voices):
            print(f"Voice {index}:")
            print(f" - ID: {voice.id}")
            print(f" - Name: {voice.name}")
            print(f" - Languages: {voice.languages}")
            print(f" - Gender: {voice.gender}")

    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

        # Voice configuration
        voices = self.engine.getProperty('voices')

        # Choose voice by ID, you can change it as your preference
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

        # Adjust speech parameters
        self.engine.setProperty('rate', 185)  # Speed (words per minute)
        self.engine.setProperty('volume', 0.9)  # 0.0 to 1.0

    def listen(self):
        """Listen for 5 seconds and return transcribed text"""
        with sr.Microphone() as source:
            print("🔴 Listening...", end='\r')
            print("🟢 Processing...", end='\r')
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=4)
            try:
                return self.recognizer.recognize_google(audio).lower()
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                print("API Unavailable")
                return ""

    def speak(self, text):
        """Convert text to speech"""
        print(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()