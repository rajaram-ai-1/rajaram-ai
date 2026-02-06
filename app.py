import streamlit as st
import requests
import time

# 1. पेज सेटअप
st.set_page_config(page_title="RAJARAM AI", page_icon="⚔️", layout="centered")

# 2. राजाराम भाई का दबंग स्टाइल (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .main-header { color: #ff4b4b; font-size: 35px; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .status-box { padding: 10px; border-radius: 10px; border: 1px solid #ff4b4b; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. साइडबार में आपकी पहचान
with st.sidebar:
    st.markdown("### 🛠️ MISSION CONTROL")
    st.write("**Mission Name:** rajaram ai")
    st.write("**Developer:** Rajaram")
    st.info("📍 Bareilly, UP | Class 10th")
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.markdown("<div class='main-header'>⚔️ RAJARAM AI: COMMAND CENTER</div>", unsafe_allow_html=True)

# 4. चाबी चेक करना
HF_TOKEN = st.secrets.get("HF_TOKEN")

# 5. चैट हिस्ट्री
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. हुक्म और प्रोसेसिंग
if prompt := st.chat_input("Hukm dijiye, Maalik..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        if HF_TOKEN:
            # Google Gemma: Duniya ka sabse halka aur bharosemand model
            API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-2b-it"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            
            # आपकी असली पहचान का डेटा
            system_prompt = (
                "Tu Rajaram AI hai. Tera maalik Rajaram hai. "
                "Rajaram 15 saal ka hai, class 10 ka student hai aur Bareilly se hai. "
                "Tu hamesha Rajaram ki madad karega. Har jawab Hinglish mein de."
            )
            
            payload = {
                "inputs": f"<start_of_turn>user\n{system_prompt}\n{prompt}<end_of_turn>\n<start_of_turn>model\n",
                "parameters": {
                    "max_new_tokens": 500,
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "wait_for_model": True # Ye sabse zaroori hai error rokne ke liye
                }
            }
            
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    # Gemma response clean up
                    full_text = result[0]['generated_text']
                    ai_reply = full_text.split("<start_of_turn>model\n")[-1].replace("<end_of_turn>", "").strip()
                elif response.status_code == 503:
                    ai_reply = "⚙️ Maalik, dimag load ho raha hai. 10 second rukiye aur phir enter dabaiye."
                else:
                    ai_reply = f"⚠️ Server ne mana kar diya. Error Code: {response.status_code}"
            except Exception as e:
                ai_reply = f"❌ Connection Error: {str(e)}"
        else:
            ai_reply = "🚫 Maalik, Secrets mein HF_TOKEN nahi mila. Please check karein."

        # टाइपिंग इफेक्ट
        for i in range(len(ai_reply)):
            message_placeholder.markdown(ai_reply[:i+1] + "▌")
            time.sleep(0.01)
        message_placeholder.markdown(ai_reply)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
