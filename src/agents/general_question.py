class GeneralQuestionAgent:
    async def run(self, query: str):
        return {
            "message": "This is a general financial question.",
            "help": "Try asking with portfolio like: AAPL 50000 TSLA 20000",
            "query": query,
            "disclaimer": "Not financial advice"
        }