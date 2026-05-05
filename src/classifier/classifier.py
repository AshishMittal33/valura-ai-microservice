class IntentClassifier:
    def __init__(self):
        pass

    async def classify(self, query: str):
        q = query.lower()

        if "portfolio" in q:
            return {"intent": "portfolio_health", "agent": "portfolio_health"}

        elif any(x in q for x in ["tell me about", "stock", "price"]):
            return {"intent": "market_research", "agent": "market_research"}

        elif any(x in q for x in ["buy", "invest"]):
            return {"intent": "investment_strategy", "agent": "investment_strategy"}

        else:
            return {"intent": "general_question", "agent": "general_question"}