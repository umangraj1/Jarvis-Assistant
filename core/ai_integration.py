import ollama
from config import settings

class MistralWrapper:
    def __init__(self):
        self.client = ollama.Client(host='http://localhost:11434')
        self.system_prompt = """
        You are Jarvis, a helpful AI assistant. Respond concisely 
        in 1-2 sentences. Formal but friendly tone.
        """

    def generate_response(self, user_input):
        response = self.client.chat(
            model='mistral',
            messages=[
                {'role': 'system', 'content': self.system_prompt},
                {'role': 'user', 'content': user_input}
            ]
        )
        return response['message']['content']
