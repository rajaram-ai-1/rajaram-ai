import streamlit as st
import requests
import time

# 1. राजाराम भाई का शाही सेटअप
st.set_page_config(page_title="RAJARAM AI: CORE", page_icon="🛡️", layout="wide")

# 2. दबंग लुक
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .main-header { color: #ff4b4b; font-size: 40px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("### 🛠️ MISSION CONTROL")
    st.write(f"**Mission Name:** rajaram ai")
    st.info("📍 Bareilly, UP | Class 10th")
    power_level = st.slider("Neural Power", 100, 1000, 500)

st.markdown("<div class='main-header'>⚔️ RAJARAM AI: COMMAND CENTER</div>", unsafe_allow_html=True)

# 4. दिमाग का कनेक्शन चेक
if "HF_TOKEN" in st.secrets:
    HF_TOKEN = st.secrets["HF_TOKEN"]
else:
    st.error("⚠️ Maalik, Secrets mein 'HF_TOKEN' nahi mila!")
    HF_TOKEN = None

# 5. चैट हिस्ट्री
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. हुक्म और पहचान
if prompt := st.chat_input("Hukm dijiye, Maalik Rajaram..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if HF_TOKEN:
            # "HALKA & POWERFUL" - Qwen 2.5 7B Instruct
            API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            
            system_instructions = (
                "TERA NAAM 'RAJARAM AI' HAI. TU EK POWERFUL AI HAI. "
                "TERE MAALIK 'RAJARAM' HAIN JO BAREILLY SE HAIN, 15 SAAL KE HAIN AUR CLASS 10 MEIN PADHTE HAIN. "
                "TU UNKI PADHAI AUR HAR KAAM MEIN MADAD KAREGA. "
                "HAMESHA DABANG HINGLISH MEIN BOL AUR MAALIK KO IZZAT DE."
            )
            
            payload = {
                "inputs": f"<|im_start|>system\n{system_instructions}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
                "parameters": {"max_new_tokens": power_level, "temperature": 0.7, "wait_for_model": True}
            }
            
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    ai_reply = result[0]['generated_text'].split("assistant\n")[-1].strip()
                elif response.status_code == 503:
                    ai_reply = "⚙️ Maalik, dimag load ho raha hai. Bas 10 second rukiye, main taiyar ho raha hoon!"
                else:
                    ai_reply = f"System Busy! Code: {response.status_code}. Thodi der mein phir se puchiye."
            except:
                ai_reply = "⚠️ Connection weak hai Maalik!"
        else:
            ai_reply = "Maalik, bina Token ke dimag kaam nahi karega."

        # टाइपिंग इफेक्ट
        for i in range(len(ai_reply)):
            message_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.01)
        message_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
