from core.voice_processing import VoiceEngine

def test_voice():
    v = VoiceEngine()
    v.speak("Testing voice system")
    command = v.listen()
    print(f"You said: {command}")

if __name__ == "__main__":
    test_voice()