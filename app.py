import streamlit as st
import requests
import sseclient
import json

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(page_title="Valura AI", layout="wide")
st.title("📊 Valura AI - Portfolio Assistant")

query = st.text_input(
    "Ask your portfolio question",
    "My portfolio has AAPL 60000 TSLA 20000 HDFC 20000. How is it doing?"
)

if st.button("Run Analysis"):
    payload = {"query": query, "context": {}}
    placeholder = st.empty()

    try:
        with requests.post(API_URL, json=payload, stream=True) as response:
            client = sseclient.SSEClient(response)

            for event in client.events():
                if not event.data:
                    continue

                data = json.loads(event.data)

                if event.event == "message":

                    stage = data.get("stage")

                    if stage == "safety":
                        placeholder.info(data["message"])

                    elif stage == "classification":
                        placeholder.info(data["message"])

                    elif stage == "classification_result":
                        st.success("Classification Done")
                        st.json(data["data"])

                    elif stage == "routing":
                        placeholder.info(data["message"])

                    elif stage == "final":
                        result = data["data"]
                        placeholder.success("✅ Final Result")

                        # 🔥 HANDLE GENERAL QUESTION (IMPORTANT FIX)
                        if "message" in result:
                            st.subheader("💬 Response")
                            st.write(result["message"])

                        if "help" in result:
                            st.info(result["help"])

                        if "query" in result:
                            st.caption(f"Query: {result['query']}")

                        # 🔥 PORTFOLIO CASE
                        if "concentration_risk" in result:
                            st.subheader("📌 Concentration Risk")
                            st.json(result["concentration_risk"])

                        if "performance" in result:
                            st.subheader("📈 Performance")
                            st.json(result["performance"])

                        if "observations" in result:
                            st.subheader("🧠 Observations")
                            for obs in result["observations"]:
                                if obs["severity"] == "warning":
                                    st.warning(obs["text"])
                                else:
                                    st.info(obs["text"])

                        # ALWAYS show disclaimer at end
                        if "disclaimer" in result:
                            st.caption(result["disclaimer"])

                elif event.event == "error":
                    placeholder.error(data["message"])
                    break

    except Exception as e:
        st.error(f"Error: {str(e)}")