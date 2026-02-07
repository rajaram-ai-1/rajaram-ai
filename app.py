import streamlit as st
import requests
import json

# --- 1. अपनी मास्टर चाबी यहाँ डालें ---
OPENROUTER_API_KEY = "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"

# --- 2. दुनिया के सबसे बेहतरीन 'फ्री' दिमागों की लिस्ट ---
# जो भी खाली होगा, कोड उसे अपने आप चुन लेगा
models_to_try = [
    "google/gemini-flash-1.5-8b:free", 
    "meta-llama/llama-3.1-8b-instruct:free", 
    "mistralai/mistral-7b-instruct:free",
    "google/gemini-flash-1.5",
    "qwen/qwen-2-7b-instruct:free"
]

def get_super_response(user_input):
    for model in models_to_try:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
                data=json.dumps({
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are Rajaram AI. A loyal brother and friend. Talk in Hindi-English. Be motivational. Take studies very seriously. Give info about jobs/exams."},
                        {"role": "user", "content": user_input}
                    ],
                    "timeout": 10
                })
            )
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'], model
        except:
            continue
    return "माफ़ करना भाई, अभी दुनिया के सभी दिमाग व्यस्त हैं।", "None"

# --- 3. सुंदर वेबसाइट का डिज़ाइन (आपकी डायरी के अनुसार) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .chat-user { background-color: #f0f2f6; padding: 15px; border-radius: 20px 20px 0px 20px; text-align: right; margin-left: auto; width: fit-content; max-width: 80%; color: black; margin-bottom: 10px; border: 1px solid #ddd; }
    .chat-ai { background-color: white; padding: 15px; border-radius: 20px 20px 20px 0px; text-align: left; margin-right: auto; width: fit-content; max-width: 80%; color: black; margin-bottom: 10px; border: 1px solid #eee; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# साइडबार
with st.sidebar:
    st.markdown("### ≡ चैट मेमोरी")
    if st.button("यादें मिटाएं"):
        st.session_state.messages = []

# हेडर
st.markdown("<h1 style='text-align: center;'>👑</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Rajaram AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>'राजाराम AI आपकी हर प्रकार से मदद करेगी और Rajaram AI आपकी मदद के लिए हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    style = "chat-user" if msg["role"] == "user" else "chat-ai"
    st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("Rajaram AI से पूछें...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='chat-user'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI खाली दिमाग ढूंढ रहा है..."):
        answer, used_model = get_super_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='chat-ai'>{answer}<br><small style='color:gray;'>दिमाग इस्तेमाल हुआ: {used_model}</small></div>", unsafe_allow_html=True)
        st.write("➕ 📷 🎥 ❤️") # डायरी के बटन्स
