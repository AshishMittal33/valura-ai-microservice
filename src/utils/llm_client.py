import os
from groq import AsyncGroq

class LLMClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        self.client = AsyncGroq(api_key=api_key) if api_key else None

    async def chat(self, messages):
        if not self.client:
            return None

        resp = await self.client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=messages,
            temperature=0,
        )

        return resp.choices[0].message.content