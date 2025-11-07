from openai import OpenAI

from ai_model.model import Model


class OpenAIModel(Model):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def request_model(self, prompt):
        pass
