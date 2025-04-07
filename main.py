# app/main.py
import streamlit as st
from app.chatbot import get_chatbot_response
from app.predictor import predict_outbreak

st.set_page_config(page_title="HealthHarmoniX", layout="centered")
st.title("HealthHarmoniX")
st.subheader("Your AI-powered multilingual health assistant")

language = st.selectbox("Select Language", ["English", "Hindi", "Telugu"])

query = st.text_input("Ask your health-related question:")

if query:
    response = get_chatbot_response(query, language)
    st.markdown("### 🤖 AI Response:")
    st.write(response)

    prediction = predict_outbreak()
    if prediction:
        st.warning(f"⚠️ {prediction}")
