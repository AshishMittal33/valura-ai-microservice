import json
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from dotenv import load_dotenv

load_dotenv()

from src.safety.guard import SafetyGuard
from src.classifier.classifier import IntentClassifier
from src.router.router import Router
from src.utils.parser import extract_portfolio

app = FastAPI()

safety = SafetyGuard()
classifier = IntentClassifier()
router = Router()


@app.post("/query")
async def query_endpoint(request: Request):
    body = await request.json()
    query = body.get("query", "")

    portfolio = extract_portfolio(query)

    async def stream():
        try:
            yield {"event": "message", "data": json.dumps({"stage": "safety", "message": "Checking safety..."})}

            s = safety.check(query)

            if s["blocked"]:
                yield {"event": "error", "data": json.dumps(s)}
                return

            yield {"event": "message", "data": json.dumps({"stage": "classification", "message": "Classifying..."})}

            c = await classifier.classify(query)

            yield {"event": "message", "data": json.dumps({"stage": "classification_result", "data": c})}

            yield {"event": "message", "data": json.dumps({"stage": "routing", "message": "Routing..."})}

            result = await router.route(c, portfolio, query)

            yield {"event": "message", "data": json.dumps({"stage": "final", "data": result})}

        except Exception as e:
            yield {"event": "error", "data": json.dumps({"message": str(e)})}

    return EventSourceResponse(stream())