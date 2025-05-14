from transformers import pipeline

class LocalLLM:
    def __init__(self):
        self.pipe = pipeline("text-generation", model="gpt2")

    def generate(self, prompt):
        return self.pipe(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']