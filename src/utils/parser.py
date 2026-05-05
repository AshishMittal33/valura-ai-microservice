import re

def extract_portfolio(query: str):
    matches = re.findall(r"([A-Za-z]+)\s*(\d+)(k?)", query)

    portfolio = []
    for ticker, value, k in matches:
        val = int(value)
        if k:
            val *= 1000

        portfolio.append({
            "ticker": ticker.upper(),
            "value": val
        })

    return portfolio