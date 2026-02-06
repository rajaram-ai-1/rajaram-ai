import streamlit as st
import requests
import time

# 1. राजाराम भाई का शाही लेआउट
st.set_page_config(page_title="RAJARAM AI: CORE", page_icon="🛡️", layout="wide")

# 2. दमदार लुक के लिए CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stMetric { background-color: #1a1a1a; padding: 15px; border-radius: 10px; border: 1px solid #ff4b4b; }
    .main-header { color: #ff4b4b; font-size: 40px; font-weight: bold; text-align: center; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar: कंट्रोल पैनल
with st.sidebar:
    st.markdown("### 🛠️ MISSION CONTROL")
    st.write(f"**Mission Name:** rajaram ai")
    st.divider()
    # AI की ताकत और मूड कंट्रोल
    power_level = st.slider("System Power (Tokens)", 100, 1000, 500)
    st.divider()
    if st.button("Emergency Shutdown"):
        st.error("System Locked by RAJARAM!")

# 4. Main Interface
st.markdown("<div class='main-header'>⚔️ RAJARAM AI: COMMAND CENTER</div>", unsafe_allow_html=True)
st.write("---")

# ऊपर 3 दमदार मीटर
col1, col2, col3 = st.columns(3)
col1.metric("System Status", "ONLINE", "Secure")
col2.metric("Neural Link", "CONNECTED", "100%")
col3.metric("Maalik", "RAJARAM", "Authorized")

st.write("---")

# 5. AI से बात करने का लॉजिक (Hugging Face के ज़रिये)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# हुक्म लेना
if prompt := st.chat_input("Hukm dijiye, Maalik..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI का जवाब तैयार करना
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # यहाँ हम Hugging Face से संपर्क करेंगे (Secrets के ज़रिये)
        # अगर अभी API Key नहीं डाली है तो ये 'Thinking' दिखाएगा
        try:
            HF_TOKEN = st.secrets["HF_TOKEN"]
            API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            
            payload = {
                "inputs": f"<|im_start|>system\nTu RAJARAM AI hai. Tera maalik RAJARAM hai. Har jawab dabang Hinglish mein de.<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
                "parameters": {"max_new_tokens": power_level, "temperature": 0.7}
            }
            
            response = requests.post(API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                full_text = response.json()[0]['generated_text']
                ai_reply = full_text.split("assistant\n")[-1].strip()
            else:
                ai_reply = "⚙️ प्रोसेसिंग... शरीर तैयार है, लेकिन दिमाग (API Key) अभी सेट नहीं किया गया है।"
        except:
            ai_reply = "⚠️ Maalik, Streamlit Settings में 'Secrets' (HF_TOKEN) डालना बाकी है।"

        # टाइपिंग इफेक्ट
        for i in range(len(ai_reply)):
            message_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.02)
        message_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
