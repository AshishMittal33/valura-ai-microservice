class GeneralQuestionAgent:
    async def run(self, query: str):
        return {
            "message": "This appears to be a general financial question.",
            "help": "You can ask about your portfolio like: AAPL 50000 TSLA 20000",
            "original_query": query,
            "disclaimer": "Not financial advice"
        }