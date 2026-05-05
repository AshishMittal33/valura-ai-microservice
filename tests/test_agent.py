import pytest
from src.agents.portfolio_health import PortfolioHealthAgent


@pytest.mark.asyncio
async def test_empty_portfolio():
    agent = PortfolioHealthAgent()
    res = await agent.run({"portfolio": []})

    assert "message" in res
    assert "disclaimer" in res


@pytest.mark.asyncio
async def test_concentration():
    agent = PortfolioHealthAgent()

    portfolio = [
        {"ticker": "AAPL", "value": 60000},
        {"ticker": "TSLA", "value": 20000},
        {"ticker": "HDFC", "value": 20000}
    ]

    res = await agent.run({"portfolio": portfolio})

    assert res["concentration_risk"]["flag"] == "high"
    assert len(res["observations"]) > 0