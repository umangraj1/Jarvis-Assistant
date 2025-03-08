from core.voice_processing import VoiceEngine
from core.ai_integration import MistralWrapper
from commands.system_commands import execute_system_command


def main():
    voice = VoiceEngine()
    ai = MistralWrapper()

    voice.speak("Hello Sir. How can I help you?")

    while True:
        command = voice.listen()
        if not command:
            continue

        # System commands first
        system_response = execute_system_command(command)
        if system_response:
            voice.speak(system_response)
            continue

        # AI fallback
        ai_response = ai.generate_response(command)
        voice.speak(ai_response)


if __name__ == "__main__":
    main()