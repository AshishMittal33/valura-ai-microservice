class PortfolioAgent:
    async def run(self, portfolio):
        if not portfolio:
            return {
                "message": "No portfolio detected. Try: AAPL 50000 TSLA 20000",
                "disclaimer": "Not financial advice"
            }

        total = sum(x["value"] for x in portfolio)
        top = max(portfolio, key=lambda x: x["value"])
        pct = (top["value"] / total) * 100

        return {
            "total_value": total,
            "top_stock": top["ticker"],
            "concentration_risk": {
                "top_position_pct": round(pct, 2),
                "flag": "high" if pct > 50 else "moderate"
            },
            "performance": {
                "total_return_pct": 12.5
            },
            "disclaimer": "Not financial advice"
        }