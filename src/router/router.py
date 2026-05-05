from src.agents.portfolio_health import PortfolioAgent
from src.agents.general_question import GeneralQuestionAgent


class Router:
    def __init__(self):
        self.portfolio_agent = PortfolioAgent()
        self.general_agent = GeneralQuestionAgent()

    async def route(self, classification, portfolio, query):
        agent = classification.get("agent")

        if agent == "portfolio_health":
            return await self.portfolio_agent.run(portfolio)

        elif agent == "general_question":
            return await self.general_agent.run(query)

        return {
            "message": "Could not understand request",
            "disclaimer": "Not financial advice"
        }