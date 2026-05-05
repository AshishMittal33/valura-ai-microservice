# 🚀 Valura AI Microservice

An AI-powered financial assistant built using FastAPI and Streamlit that analyzes user queries, detects intent, applies safety checks, and provides portfolio insights via a modular agent-based architecture.

---

## 📌 Features

* Intent Classification (rule-based, low latency)
* Safety Guard (blocks harmful financial queries)
* Agent-based Architecture (modular & scalable)
* Portfolio Analysis (risk & concentration insights)
* SSE Streaming (real-time responses)
* Streamlit Frontend (interactive UI)
* Natural Language Parsing (extract portfolio from query)

---

## 🏗️ Architecture

User → Streamlit → FastAPI → Parser → Safety → Classifier → Router → Agent → SSE → UI

---

## 📁 Project Structure

src/

├── main.py # API entry point (SSE streaming)

├── safety/

│   └── guard.py  # Safety validation layer

├── classifier/

│   └── classifier.py       # Intent classification logic
├── router/

│   └── router.py           # Routes request to correct agent
├── agents/

│   ├── portfolio_health.py # Portfolio analysis agent

│   └── general_question.py # General query handler
├── utils/

│   └── parser.py           # Extract portfolio from text

app.py                      # Streamlit frontend
.env                        # Environment variables

---

## 🔄 Flow Explanation

1. User sends query
2. Parser extracts portfolio data
3. Safety guard blocks harmful inputs
4. Classifier determines intent
5. Router selects appropriate agent
6. Agent generates response
7. Response streamed back via SSE

---

## 🧠 Example Queries

Portfolio Analysis:
~~~
My portfolio has AAPL 60000 TSLA 20000 HDFC 20000
~~~
Blocked Query:
~~~
How to manipulate stock price?
~~~
General Question:
~~~
What is market manipulation?
~~~
---

## 📊 Sample Output

{
"concentration_risk": {
"top_position_pct": 60.0,
"flag": "high"
},
"performance": {
"total_return_pct": 12.5
}
}

---

## ⚙️ Installation

git clone <repo-url>
cd valura-ai-microservice
pip install -r requirements.txt

---

## 🔑 Environment Variables

Create .env file:

GROQ_API_KEY=your_api_key_here

---

## ▶️ Run Backend
```
uvicorn src.main:app --reload
```
---

## 🎨 Run Frontend
```
streamlit run app.py
```
---

## 🧪 Testing

You can test using Thunder Client, Postman, Curl, or the Streamlit UI.

---

## ⚡ Design Decisions

Rule-based Classifier: Faster, no dependency, low latency
Agent-based Architecture: Modular and scalable
SSE Streaming: Real-time response handling
Natural Language Parsing: No manual input required

---

## ⚠️ Limitations

* Regex-based portfolio parsing
* No real-time market data
* Basic classification logic

---

## 🚀 Future Improvements

* Integrate real stock APIs (yfinance)
* Upgrade classifier to LLM
* Add more agents (risk scoring, recommendations)
* Use Pydantic models
* Add database support

---

## 💬 Final Note

This project demonstrates a production-style backend system using modular architecture, streaming responses, and safety-first AI design.

---

## 📢 Disclaimer

This system does not provide financial advice.
All outputs are for educational purposes only.
