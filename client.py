# =====================================================================
# MODULE 3: CLIENT.PY - STREAMLIT CONVERSATIONAL CHAT UI
# =====================================================================
import streamlit as st
import requests

st.set_page_config(page_title="DevReview AI Chat", page_icon="🤖", layout="centered")
st.title("🤖 DevReview AI: Code Audit Terminal")

API_SERVER_URL = "http://127.0.0.1:8000/v1/chat/completions"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Paste a code snippet..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        try:
            payload = {"prompt": user_input, "max_tokens": 128}
            api_call = requests.post(API_SERVER_URL, json=payload, timeout=45)
            if api_call.status_code == 200:
                json_data = api_call.json()
                ai_text = json_data["response"]
                latency_info = json_data["latency_seconds"]
                full_display = f"{ai_text}\n\n---\n⏱️ *Inference Latency: {latency_info}s*"
                response_placeholder.markdown(full_display)
                st.session_state.messages.append({"role": "assistant", "content": full_display})
            else:
                response_placeholder.markdown(f"❌ API Server Error: {api_call.status_code}")
        except requests.exceptions.ConnectionError:
            response_placeholder.markdown("❌ Connection Error: Ensure your FastAPI backend server is running on port 8000!")
