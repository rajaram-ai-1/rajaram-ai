import streamlit as st
import requests
import json

# --- 1. अपनी मास्टर चाबी यहाँ डालें ---
OPENROUTER_API_KEY = "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"

# --- 2. दिमागों की सूची (जो खाली होगा वो काम करेगा) ---
# हमने यहाँ उन मॉडल्स को रखा है जो अक्सर फ्री या बहुत सस्ते होते हैं
models_to_try = [
    "google/gemini-flash-1.5", 
    "meta-llama/llama-3.1-8b-instruct:free", 
    "mistralai/mistral-7b-instruct:free",
    "google/gemini-pro-1.5"
]

def get_smart_response(user_input):
    # यह लूप खुद ही 'खाली दिमाग' ढूंढेगा
    for model_name in models_to_try:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": "You are Rajaram AI. Friendly brother and mentor. Motivational."},
                        {"role": "user", "content": user_input}
                    ]
                }),
                timeout=10 # अगर 10 सेकंड में जवाब न मिले तो अगला मॉडल देखो
            )
            
            if response.status_code == 200:
                res_json = response.json()
                return res_json['choices'][0]['message']['content']
            else:
                # अगर इस मॉडल का कोटा खत्म है (429) या कोई और दिक्कत है, तो अगले पर बढ़ो
                print(f"{model_name} व्यस्त है, अगले दिमाग पर जा रहा हूँ...")
                continue
                
        except Exception:
            continue
            
    return "माफ़ करना राजाराम भाई, अभी सभी जादुई दिमाग थके हुए हैं। 1 मिनट इंतज़ार करें।"

# --- 3. सुंदर वेबसाइट का इंटरफ़ेस ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

# CSS: सफ़ेद बैकग्राउंड और साफ़ लुक
st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    .chat-box { border: 1px solid #ddd; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .title-text { text-align: center; font-weight: bold; font-size: 35px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title-text'>👑 Rajaram AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><i>'आपका भाई, आपका मार्गदर्शक'</i></p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट दिखाना
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# इनपुट
prompt = st.chat_input("भाई से कुछ भी पूछो...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("राजाराम AI खाली दिमाग ढूंढ रहा है..."):
            answer = get_smart_response(prompt)
            st.write(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
