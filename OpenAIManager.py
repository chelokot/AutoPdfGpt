import openai

class OpenAIManager:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_answer(self, prompt):
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': prompt}]
        
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = completions.choices[0].message['content']
        return message
