import streamlit as st
import requests
from datetime import datetime, timedelta

# --- CONFIGURATION & SECRETS ---
# Streamlit Secrets se keys fetch karna
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

st.set_page_config(page_title="Rajaram AI", layout="wide")

# --- UI CUSTOM CSS (For Buttons Position) ---
st.markdown("""
    <style>
    .stButton > button { width: 100%; border-radius: 20px; }
    /* Floating action buttons style logic can be added here */
    </style>
    """, unsafe_allow_html=True)

## --- FUNCTIONS ---

def get_latest_news():
    # 10-15 minute pehle ki news ke liye filter
    ten_mins_ago = (datetime.now() - timedelta(minutes=15)).strftime('%Y-%m-%dT%H:%M:%S')
    url = f"https://newsapi.org/v2/everything?q=latest&from={ten_mins_ago}&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    return response.get('articles', [])[:5]

def generate_meta_content(prompt, mode="text"):
    # Yahan Meta ke Llama 3 ya Imagine model ki API call hogi
    # Example using a placeholder for Meta's API logic
    return f"Rajaram AI Response for {prompt} using Meta Model"

## --- SIDEBAR & BUTTONS ---

# Left Side: Upload Button (+)
with st.sidebar:
    st.title("➕ Upload Center")
    uploaded_file = st.file_uploader("Photo/Video Upload karein", type=["jpg", "png", "mp4"])
    if uploaded_file:
        st.success("File Upload Ho Gayi!")

# Right Side (Main UI): Live Chat Button
col1, col2, col3 = st.columns([1, 6, 1])
with col3:
    if st.button("🎤 LIVE"):
        st.toast("Live Voice Chat Shuru Ho Raha Hai...")

## --- MAIN CHAT INTERFACE ---

st.title("🤖 Rajaram AI (Meta Powered)")

# Taja Khabar Section
if st.button("🌍 10 Minute Pehle Ki Taja Khabar"):
    news = get_latest_news()
    for article in news:
        st.write(f"**{article['title']}** - {article['source']['name']}")

# Chat Input
user_input = st.chat_input("Mujhse kuch bhi puchein ya Image/Video banane ko kahein...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        # Logic to detect if user wants image or text
        if "photo" in user_input.lower() or "image" in user_input.lower():
            st.write("Meta Imagine se Photo ban rahi hai...")
            # st.image(api_call_to_meta_image(user_input))
        else:
            response = generate_meta_content(user_input)
            st.write(response)
