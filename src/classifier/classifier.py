import json
import re
from src.utils.llm_client import LLMClient


class IntentClassifier:
    def __init__(self):
        self.llm = LLMClient()

    async def classify(self, query: str):
        q = query.lower()

        # 🔥 HARD RULES (prevent LLM stupidity)
        if "portfolio" in q or any(char.isdigit() for char in q):
            return {"intent": "portfolio_health", "agent": "portfolio_health"}

        if not any(char.isdigit() for char in q):
            return {"intent": "general_question", "agent": "general_question"}

        # 🔥 LLM fallback
        prompt = f"""
Classify into:
portfolio_health, market_research, investment_strategy, general_question

Return ONLY JSON:
{{"intent": "...", "agent": "..."}}

Query: {query}
"""

        try:
            raw = await self.llm.chat([
                {"role": "user", "content": prompt}
            ])

            match = re.search(r"\{.*\}", raw, re.DOTALL)
            data = json.loads(match.group(0))

            valid = [
                "portfolio_health",
                "market_research",
                "investment_strategy",
                "general_question"
            ]

            if data.get("agent") not in valid:
                raise ValueError()

            return data

        except:
            return {"intent": "general_question", "agent": "general_question"}