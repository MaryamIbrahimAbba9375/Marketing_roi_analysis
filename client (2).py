# =====================================================================
# MODULE 4: CLIENT.PY - STREAMLIT FRONTEND MILESTONE
# =====================================================================
import streamlit as st
import requests

st.set_page_config(page_title="ImagiServe Studio", page_icon="🎨", layout="centered")
st.title("🎨 ImagiServe Studio: Interior Design Concept Hub")

API_URL = "http://127.0.0.1:8000/generate/image"

# Milestone 4: Initialize session_state tracking for structural chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messaging canvas layouts
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["type"] == "text":
            st.markdown(message["content"])
        elif message["type"] == "image":
            st.image(message["content"])

# Milestone 4: Use st.chat_input for user interactive prompt loops
if user_prompt := st.chat_input("Describe an interior design layout (e.g., 'A minimalist scandinavian living room with oak accents')..."):
    
    # Store and render text input component
    st.session_state.messages.append({"role": "user", "type": "text", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)
        
    # Query API endpoint interface
    with st.chat_message("assistant"):
        with st.spinner("Synthesizing rendering mockups..."):
            try:
                # Issue standard HTTP GET request with URL parameters
                params = {"prompt": user_prompt, "negative_prompt": "blurry, dark, low quality, bad architecture"}
                response = requests.get(API_URL, params=params, timeout=90)
                
                if response.status_code == 200:
                    # Milestone 4: Render binary content data immediately with st.image
                    st.image(response.content, caption="Generated Concept Output Layout")
                    st.session_state.messages.append({"role": "assistant", "type": "image", "content": response.content})
                else:
                    st.error(f"❌ Server Return Exception Code: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Connection Error: Is your FastAPI microservice background worker running on port 8000?")
