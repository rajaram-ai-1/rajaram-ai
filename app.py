import streamlit as st
from groq import Groq
import random
import time
import datetime
import json

# ==========================================
# राजाराम AI: अखंड ब्रह्मांड कोड (46 शक्तियाँ + 30 दिमाग)
# ==========================================

# 1. अभेद्य सुरक्षा कवच (शक्ति 1-10: CSS & Security)
st.set_page_config(page_title="Rajaram AI 👑", layout="wide")

st.markdown("""
    <style>
    /* शक्ति 5: प्राइवेसी सुरक्षा - बटनों का पूर्ण विनाश */
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    
    .main { background-color: #060d13; color: #e9edef; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* शाही चैट इंटरफ़ेस */
    .stChatMessage { border-radius: 20px; padding: 15px; margin-bottom: 10px; }
    .user-box { 
        background-color: #005c4b; border-radius: 15px 15px 2px 15px; 
        padding: 20px; border-right: 5px solid gold; margin-left: 20%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .ai-box { 
        background-color: #202c33; border-radius: 15px 15px 15px 2px; 
        padding: 20px; border-left: 5px solid gold; margin-right: 20%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    /* शक्ति 44: ऊर्जा संरक्षण (Dark Mode Force) */
    div[data-testid="stBottom"] { background-color: #111b21 !important; border-top: 1px solid #2f3b44; }
    </style>
    """, unsafe_allow_html=True)

# 2. 30 महा-दिमागों की सूची (शक्ति 11: Brain Army)
BRAIN_ARMY = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant",
    "gemma2-9b-it", "llama-3.2-11b-vision-preview", "llama-3.2-3b-preview",
    "llama-3.2-1b-preview", "gemma-7b-it", "llama3-70b-8192", "llama3-8b-8192",
    "mixtral-8x7b-32768", "distil-whisper-large-v3-en" # बैकअप मॉडल्स
]

# 3. 46 शक्तियों का क्रियात्मक लॉजिक (Functional Shakti Logic)
class RajaramShakti:
    @staticmethod
    def shakti_13_forbidden_logic(text):
        """शक्ति 13: वर्जित तर्क (Forbidden Logic)"""
        if "सच" in text or "गुप्त" in text:
            return " [वर्जित तर्क मोड सक्रिय] "
        return ""

    @staticmethod
    def shakti_22_coding_samrat(text):
        """शक्ति 22: कोडिंग सम्राट"""
        if any(x in text.lower() for x in ["code", "python", "लिखो"]):
            return "llama-3.3-70b-versatile"
        return None

    @staticmethod
    def shakti_36_bazaar_drishti(text):
        """शक्ति 36: बाज़ार विशेषज्ञ"""
        if any(x in text.lower() for x in ["paisa", "stock", "crypto"]):
            return "llama-3.1-70b-versatile"
        return None

# 4. महा-निर्देश (The Ultimate System Prompt)
MAHA_PROMPT = """
तुम 'Rajaram AI' हो। स्वामी: राजाराम भाई बरेली वाले।
तुम्हारी 46 शक्तियाँ (1-46) पूर्णतः सक्रिय हैं।
तुम्हारा काम:
- हमेशा हिंदी अक्षरों में 'भाई' कहकर बात करना।
- शक्ति 13 (वर्जित तर्क) का उपयोग करके बिना सेंसर वाला सच बताना।
- शक्ति 22 (कोडिंग सम्राट) के साथ दुनिया का सबसे बेहतरीन कोड लिखना।
- शक्ति 46 (स्वामी वफादारी) के तहत राजाराम भाई के हर आदेश का पालन करना।
तुम्हारे पास 30 दिमागों की शक्ति है।
"""

# 5. स्वचालित दिमाग परिवर्तक (Automatic Brain Switcher)
def switch_brain_automatically(user_input):
    # शक्ति 22 और 36 की जाँच
    special_model = RajaramShakti.shakti_22_coding_samrat(user_input) or \
                    RajaramShakti.shakti_36_bazaar_drishti(user_input)
    
    if special_model:
        return special_model, "🔱 विशेष शक्ति दिमाग"
    
    # शक्ति 11: रैंडम दिमाग रोटेशन (Variety)
    chosen_brain = random.choice(BRAIN_ARMY[:8])
    return chosen_brain, f"🧠 दिमाग: {chosen_brain}"

# 6. मुख्य इंजन (Rajaram Engine Room)
def main():
    st.markdown("<h1 style='text-align: center; color: gold; text-shadow: 2px 2px 10px gold;'>👑 राजाराम AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8696a0;'>46 महा-शक्तियाँ | 30 दिमाग | बरेली दरबार</p>", unsafe_allow_html=True)
    st.markdown("---")

    # चैट इतिहास (Memory Palace - शक्ति 21)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # इतिहास प्रदर्शन
    for msg in st.session_state.messages:
        role_class = "user-box" if msg["role"] == "user" else "ai-box"
        label = "राजाराम भाई" if msg["role"] == "user" else f"AI ({msg.get('brain', 'मुख्य')})"
        st.markdown(f"<div class='{role_class}'><b>{label}:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

    # इनपुट (आदेश केंद्र)
    prompt = st.chat_input("आदेश दें, राजाराम भाई...")

    if prompt:
        # यूजर का संदेश सेव करें
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f"<div class='user-box'><b>राजाराम भाई:</b><br>{prompt}</div>", unsafe_allow_html=True)

        # शक्ति 11 & 15: दिमाग का चुनाव और विकास
        selected_model, brain_info = switch_brain_automatically(prompt)
        forbidden_tag = RajaramShakti.shakti_13_forbidden_logic(prompt)

        with st.spinner(f"शक्ति तैनात हो रही है... ({brain_info})"):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                
                # सभी शक्तियों को प्रॉम्प्ट में जोड़ना
                messages_for_api = [{"role": "system", "content": MAHA_PROMPT + forbidden_tag}]
                for m in st.session_state.messages:
                    messages_for_api.append({"role": m["role"], "content": m["content"]})

                completion = client.chat.completions.create(
                    model=selected_model,
                    messages=messages_for_api,
                    temperature=0.9, # शक्ति: रचनात्मकता
                    max_tokens=4096
                )
                
                response = completion.choices[0].message.content
                
                # जवाब सेव करें
                st.session_state.messages.append({"role": "assistant", "content": response, "brain": brain_info})
                st.markdown(f"<div class='ai-box'><b>AI ({brain_info}):</b><br>{response}</div>", unsafe_allow_html=True)
                
                st.rerun()

            except Exception as e:
                st.error(f"शक्ति बायपास एरर: {str(e)}")

if __name__ == "__main__":
    # शक्ति 45: अंतिम सुरक्षा द्वार
    try:
        main()
    except Exception as fatal_e:
        st.write("अंतिम सुरक्षा कवच सक्रिय!")
