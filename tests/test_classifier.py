import pytest
from unittest.mock import AsyncMock
from src.classifier.classifier import IntentClassifier


@pytest.mark.asyncio
async def test_portfolio_health(mocker):
    clf = IntentClassifier()

    mocker.patch.object(
        clf.llm,
        "chat",
        AsyncMock(
            return_value='{"intent":"portfolio_health","agent":"portfolio_health","entities":{"tickers":[],"amount":null,"period_years":null},"safety":"safe"}'
        ),
    )

    res = await clf.classify("How is my portfolio doing?")
    assert res["agent"] == "portfolio_health"


@pytest.mark.asyncio
async def test_market_research(mocker):
    clf = IntentClassifier()

    mocker.patch.object(
        clf.llm,
        "chat",
        AsyncMock(
            return_value='{"intent":"market_research","agent":"market_research","entities":{"tickers":["AAPL"],"amount":null,"period_years":null},"safety":"safe"}'
        ),
    )

    res = await clf.classify("Tell me about AAPL")
    assert res["agent"] == "market_research"
    assert "AAPL" in res["entities"]["tickers"]


@pytest.mark.asyncio
async def test_investment_strategy(mocker):
    clf = IntentClassifier()

    mocker.patch.object(
        clf.llm,
        "chat",
        AsyncMock(
            return_value='{"intent":"investment_strategy","agent":"investment_strategy","entities":{"tickers":["TSLA"],"amount":null,"period_years":null},"safety":"safe"}'
        ),
    )

    res = await clf.classify("Should I buy Tesla?")
    assert res["agent"] == "investment_strategy"