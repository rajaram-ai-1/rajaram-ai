import streamlit as st
import requests
import time

# 1. राजाराम भाई का मिशन सेटअप
st.set_page_config(page_title="RAJARAM AI: LITE", page_icon="⚡", layout="wide")

# 2. लुक और फील
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .main-header { color: #00ffcc; font-size: 35px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. साइडबार में आपकी पहचान
with st.sidebar:
    st.markdown("### 🛠️ MISSION CONTROL")
    st.write(f"**Developer:** Rajaram (Bareilly)")
    st.write(f"**Age:** 15 | **Class:** 10th")
    st.success("Target: Lightest Brain Active")

st.markdown("<div class='main-header'>⚡ RAJARAM AI: FAST MODE</div>", unsafe_allow_html=True)

# 4. तिजोरी से चाबी निकालना
HF_TOKEN = st.secrets.get("HF_TOKEN")

# 5. चैट हिस्ट्री
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. हुक्म और Google Gemma का दिमाग
if prompt := st.chat_input("Puchiye Maalik..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if HF_TOKEN:
            # DUNIA KA SABSE HALKA DIMAG: Google Gemma 2B
            API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-2b-it"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            
            # आपकी बरेली वाली पहचान
            system_info = "Tu Rajaram AI hai. Tera maalik Rajaram (15 saal, 10th class, Bareilly) hai. Tu bahut fast aur chota model hai par dimag tez hai."
            
            payload = {
                "inputs": f"{system_info}\nUser: {prompt}\nAI:",
                "parameters": {"max_new_tokens": 250, "temperature": 0.6}
            }
            
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    # Gemma का जवाब निकालने का तरीका
                    ai_reply = result[0]['generated_text'].split("AI:")[-1].strip()
                else:
                    ai_reply = f"Maalik, server thoda slow hai (Error: {response.status_code}). Ek baar phir enter dabaiye!"
            except:
                ai_reply = "⚠️ Link toot gaya, phir se koshish karein."
        else:
            ai_reply = "Maalik, Secrets mein HF_TOKEN nahi mila."

        # टाइपिंग इफेक्ट
        for i in range(len(ai_reply)):
            message_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.01)
        message_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
