from app.llm import LLMClient


class Agent:

    def __init__(self, llm: LLMClient):

        self.llm = llm

        self.system_message = {
            "role": "system",
            "content": """
            You are a helpful AI assistant.
            Answer clearly and accurately.
            If you do not know something, say so.
            Respond in the same language as the user.
            Your developer's name is Amir
            """
        }

        self.messages = [self.system_message.copy()]

    def run(self, user_input: str) -> str:

        if not user_input.strip():
            raise ValueError("User input cannot be empty")

        self.messages.append({
            "role": "user",
            "content": user_input,
        })

        try:
            response = self.llm.generate(self.messages)

        except Exception:
            self.messages.pop()
            raise

        self.messages.append({
            "role": "assistant",
            "content": response,
        })

        return response

    def reset(self):

        self.messages = [self.system_message.copy()]