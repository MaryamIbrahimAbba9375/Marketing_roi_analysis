# =====================================================================
# MODULE 4: CLIENT.PY - STREAMLIT DYNAMIC CREATIVE PORTAL
# =====================================================================
import streamlit as st
import requests

st.set_page_config(page_title="ImagiServe Studio", page_icon="🎨", layout="centered")
st.title("🎨 ImagiServe Studio: Concept Creative Engine")
st.caption("FastAPI Microservice backend streaming a distilled Stable Diffusion architecture.")

API_URL = "http://127.0.0.1:8000/generate/image"

user_prompt = st.text_area("Creative Art Prompt Input:", placeholder="A modern sleek smartphone sitting on an obsidian stone desk, commercial photography...")
neg_prompt = st.text_input("Negative Quality Bounds Filter:", value="blurry, low quality, text overlay, watermarks")

if st.button("Synthesize Artwork Assets"):
    if not user_prompt.strip():
        st.warning("Please insert an architectural string prompt direction.")
    else:
        with st.spinner("Executing structural layer calculation passes via FastAPI..."):
            try:
                payload = {"prompt": user_prompt, "negative_prompt": neg_prompt}
                response = requests.post(API_URL, json=payload, timeout=90)
                
                if response.status_code == 200:
                    # Dynamically render response content bytes without intermediate disk writes
                    st.image(response.content, caption="Synthesized Artwork Asset Result", use_container_width=True)
                    st.success("✅ Frame buffer streaming passed successfully!")
                else:
                    st.error(f"❌ API Processing Flag Defect: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Connection Defect: Is your FastAPI endpoint active at localhost:8000?")
