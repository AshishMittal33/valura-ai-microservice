import streamlit as st
import requests
import sseclient
import json

API_URL = "http://127.0.0.1:8000/query"

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Valura AI",
    page_icon="📊",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align: center;'>📊 Valura AI</h1>
<p style='text-align: center; color: gray;'>Smart Portfolio Analysis with AI</p>
""", unsafe_allow_html=True)

st.divider()

# ---------- INPUT SECTION ----------
with st.container():
    st.subheader("💬 Ask Your Query")

    query = st.text_input(
        "Enter your query",
        "My portfolio has AAPL 60000 TSLA 20000",
        label_visibility="collapsed"
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        run_button = st.button("🚀 Run Analysis", use_container_width=True)

st.divider()

# ---------- RESPONSE SECTION ----------
if run_button:

    payload = {"query": query}

    with st.spinner("Analyzing..."):
        try:
            with requests.post(API_URL, json=payload, stream=True) as response:
                client = sseclient.SSEClient(response)

                for event in client.events():
                    if not event.data:
                        continue

                    data = json.loads(event.data)

                    if event.event == "message":

                        stage = data.get("stage")

                        # -------- STATUS ----------
                        if stage == "safety":
                            st.info("🔒 Checking safety...")

                        elif stage == "classification":
                            st.info("🧠 Classifying query...")

                        elif stage == "routing":
                            st.info("🔀 Routing request...")

                        elif stage == "classification_result":
                            with st.expander("🧠 Classification Details"):
                                st.json(data["data"])

                        # -------- FINAL RESULT ----------
                        elif stage == "final":
                            result = data["data"]

                            st.success("✅ Analysis Complete")

                            st.divider()

                            # -------- GENERAL RESPONSE ----------
                            if "message" in result:
                                st.subheader("💬 Response")
                                st.write(result["message"])

                            if "help" in result:
                                st.info(result["help"])

                            # -------- PORTFOLIO METRICS ----------
                            if "total_value" in result:
                                col1, col2 = st.columns(2)

                                col1.metric("💰 Total Value", f"${result['total_value']:,}")
                                col2.metric("🏆 Top Stock", result["top_stock"])

                            if "concentration_risk" in result:
                                risk = result["concentration_risk"]

                                st.subheader("📊 Risk Analysis")

                                col1, col2 = st.columns(2)

                                col1.metric("Top Position %", f"{risk['top_position_pct']}%")
                                col2.metric("Risk Level", risk["flag"].upper())

                            if "performance" in result:
                                st.subheader("📈 Performance")
                                st.metric(
                                    "Return %",
                                    f"{result['performance']['total_return_pct']}%"
                                )

                            # -------- DISCLAIMER ----------
                            if "disclaimer" in result:
                                st.divider()
                                st.caption(result["disclaimer"])

                    elif event.event == "error":
                        st.error(data["message"])

        except Exception as e:
            st.error(f"Error: {str(e)}")