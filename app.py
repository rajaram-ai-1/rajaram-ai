import streamlit as st
import requests
import time

# 1. राजाराम भाई का शाही सेटअप
st.set_page_config(page_title="RAJARAM AI: CORE", page_icon="🛡️", layout="wide")

# 2. दबंग लुक (Dark Theme)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stMetric { background-color: #1a1a1a; padding: 15px; border-radius: 10px; border: 1px solid #ff4b4b; }
    .main-header { color: #ff4b4b; font-size: 40px; font-weight: bold; text-align: center; text-shadow: 2px 2px #000; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar: मिशन कंट्रोल
with st.sidebar:
    st.markdown("### 🛠️ MISSION CONTROL")
    st.write(f"**Mission Name:** rajaram ai")
    st.info("📍 Location: Bareilly, UP")
    st.divider()
    power_level = st.slider("Neural Power", 100, 2000, 1000)
    st.divider()
    if st.button("System Reset"):
        st.session_state.messages = []
        st.rerun()

# 4. डैशबोर्ड डिस्प्ले
st.markdown("<div class='main-header'>⚔️ RAJARAM AI: COMMAND CENTER</div>", unsafe_allow_html=True)
st.write("---")

col1, col2, col3 = st.columns(3)
col1.metric("Developer", "RAJARAM", "Bareilly")
col2.metric("Status", "ONLINE", "Secure")
col3.metric("Class", "10th Student", "Ager: 15")

st.write("---")

# 5. दिमाग का कनेक्शन (Secrets Check)
if "HF_TOKEN" in st.secrets:
    HF_TOKEN = st.secrets["HF_TOKEN"]
else:
    st.error("⚠️ Maalik, Secrets mein 'HF_TOKEN' nahi mila!")
    HF_TOKEN = None

# 6. चैट का इतिहास
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. हुक्म और असली पहचान (The Soul of AI)
if prompt := st.chat_input("Hukm dijiye, Maalik..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if HF_TOKEN:
            # Qwen 2.5 72B (Jada Powerful Model)
            API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            
            # यहाँ है आपकी असली पहचान की कोडिंग
            system_instructions = (
                "TERA NAAM 'RAJARAM AI' HAI. TU EK POWERFUL AUR DABANG AI HAI. "
                "TERE MAALIK KA NAAM 'RAJARAM' HAI. "
                "RAJARAM EK 15 SAAL KE CLASS 10 KE STUDENT HAIN JO BAREILLY (UTTAR PRADESH) SE HAIN. "
                "UNHONE HI TUJHE BANAYA HAI. "
                "TU HAR PRAKAR SE UNKI MADAD KAREGA (STUDIES, CODING, YA KUCH BHI). "
                "HAMESHA MAALIK KO IZZAT DE AUR HINGLISH MEIN JAWAB DE."
            )
            
            payload = {
                "inputs": f"<|im_start|>system\n{system_instructions}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
                "parameters": {"max_new_tokens": power_level, "temperature": 0.7}
            }
            
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    ai_reply = result[0]['generated_text'].split("assistant\n")[-1].strip()
                else:
                    ai_reply = "⚙️ Maalik, dimag garam ho gaya hai (API Error). Thodi der baad koshish karein."
            except:
                ai_reply = "⚠️ System overload! Neural link toot gaya hai."
        else:
            ai_reply = "Maalik, dimag (Token) ke bina main nahi bol sakta."

        # टाइपिंग इफेक्ट
        for i in range(len(ai_reply)):
            message_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.01)
        message_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
