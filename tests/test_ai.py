from core.ai_integration import MistralWrapper

def test_mistral():
    ai = MistralWrapper()
    print(ai.generate_response("What's the capital of India?"))

if __name__ == "__main__":
    test_mistral()