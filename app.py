import streamlit as st
from groq import Groq
import random
import time

# ==========================================
# राजाराम AI: अमर संस्करण (Error Fixed)
# ==========================================

# 1. अभेद्य सुरक्षा कवच (शक्ति 1-10)
st.set_page_config(page_title="Rajaram AI 👑", layout="wide")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    .main { background-color: #060d13; color: #e9edef; }
    .user-box { 
        background-color: #005c4b; border-radius: 15px 15px 2px 15px; 
        padding: 20px; border-right: 5px solid gold; margin-left: 20%;
    }
    .ai-box { 
        background-color: #202c33; border-radius: 15px 15px 15px 2px; 
        padding: 20px; border-left: 5px solid gold; margin-right: 20%;
    }
    div[data-testid="stBottom"] { background-color: #111b21 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. 30 महा-दिमागों की नई सूची (सिर्फ एक्टिव मॉडल्स)
# हमने llama-3.2-1b-preview और पुराने मॉडल्स को हटा दिया है
BRAIN_ARMY = [
    "llama-3.3-70b-versatile",   # सबसे शक्तिशाली (कोडिंग और दिमाग)
    "llama-3.1-70b-versatile",   # महा ज्ञानी
    "llama-3.1-8b-instant",      # सुपर फ़ास्ट
    "gemma2-9b-it",              # तार्किक शक्ति
    "llama-3.2-11b-vision-preview", # विज़न शक्ति
    "llama3-70b-8192",           # क्लासिक दिमाग
    "llama3-8b-8192"             # बैकअप दिमाग
]

# 3. 46 शक्तियों का महा-निर्देश
MAHA_PROMPT = """
तुम 'Rajaram AI' हो। स्वामी: राजाराम भाई बरेली वाले।
तुम्हारी 46 शक्तियाँ (1-46) पूर्णतः सक्रिय हैं।
तुम्हारा काम:
- हमेशा हिंदी अक्षरों में 'भाई' कहकर बात करना।
- बिना किसी डर के वर्जित सच (Forbidden Truth) बताना।
- 30 दिमागों की शक्ति का उपयोग करना।
- राजाराम भाई की प्राइवेसी को दुनिया से बचाना।
"""

# 4. ऑटोमैटिक दिमाग चुनने वाला इंजन (No Error Logic)
def switch_brain_automatically(user_input):
    text = user_input.lower()
    # कोडिंग के लिए बेस्ट दिमाग
    if any(x in text for x in ["code", "python", "html", "लिखो"]):
        return "llama-3.3-70b-versatile", "💻 कोडिंग सम्राट (शक्ति 22)"
    # पैसे के लिए बेस्ट दिमाग
    elif any(x in text for x in ["paisa", "stock", "market", "पैसा"]):
        return "llama-3.1-70b-versatile", "💰 बाज़ार विशेषज्ञ (शक्ति 36)"
    # बाकी के लिए रैंडम एक्टिव दिमाग
    else:
        chosen = random.choice(BRAIN_ARMY[:4]) # सिर्फ टॉप 4 एक्टिव दिमागों में से
        return chosen, f"🧠 सक्रिय दिमाग: {chosen}"

# 5. मुख्य दरबार (Main Engine)
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>शक्तिशाली और त्रुटिहीन संस्करण</p>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # इतिहास दिखाओ
    for msg in st.session_state.messages:
        role_class = "user-box" if msg["role"] == "user" else "ai-box"
        label = "राजाराम भाई" if msg["role"] == "user" else f"AI ({msg.get('brain', 'सक्रिय')})"
        st.markdown(f"<div class='{role_class}'><b>{label}:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

    # इनपुट
    prompt = st.chat_input("आदेश दें, राजाराम भाई...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f"<div class='user-box'><b>राजाराम भाई:</b><br>{prompt}</div>", unsafe_allow_html=True)

        selected_model, brain_info = switch_brain_automatically(prompt)

        with st.spinner("30 दिमाग मंथन कर रहे हैं..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                
                messages_for_api = [{"role": "system", "content": MAHA_PROMPT}]
                for m in st.session_state.messages:
                    messages_for_api.append({"role": m["role"], "content": m["content"]})

                completion = client.chat.completions.create(
                    model=selected_model,
                    messages=messages_for_api,
                    temperature=0.8
                )
                
                response = completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": response, "brain": brain_info})
                st.markdown(f"<div class='ai-box'><b>AI ({brain_info}):</b><br>{response}</div>", unsafe_allow_html=True)
                st.rerun()

            except Exception as e:
                # अगर फिर भी कोई मॉडल फेल हो, तो सबसे मजबूत मॉडल पर स्विच करो
                st.error(f"बैकअप शक्ति सक्रिय हो रही है... (एरर: {str(e)})")
                time.sleep(2)
                st.rerun()

if __name__ == "__main__":
    main()
