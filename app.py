import streamlit as st
from groq import Groq
import random
from gtts import gTTS
import base64
import os

# --- 1. शाही सेटअप ---
st.set_page_config(page_title="Rajaram AI 👑", layout="centered")
st.markdown("""
    <style>
    header, footer, .stAppDeployButton {visibility: hidden !important;}
    .main { background-color: #0b141a; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. बोलने की शक्ति ---
def shakti_speak(text):
    try:
        if os.path.exists("reply.mp3"):
            os.remove("reply.mp3")
        tts = gTTS(text=text, lang='hi')
        tts.save("reply.mp3")
        with open("reply.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
            st.markdown(f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>', unsafe_allow_html=True)
    except:
        pass

# --- 3. 2026 के सबसे नए दिमागों की फौज ---
# यहाँ हमने सिर्फ वही रखे हैं जो 'अमर' हैं और Groq पर अभी चल रहे हैं
MODELS_ARMY = [
    "llama-3.3-70b-versatile",  # सबसे शक्तिशाली
    "llama-3.1-8b-instant",     # सबसे तेज़
    "llama-3.2-11b-vision-preview", # नया मॉडल
    "llama-3.2-3b-preview"      # छोटा और फुर्तीला
]

# --- 4. मुख्य इंजन ---
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI दरबार</h1>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # लिखने वाला बॉक्स
    prompt = st.chat_input("हुकुम करें, राजाराम भाई...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # दिमाग का चुनाव
            selected_brain = random.choice(MODELS_ARMY)
            
            with st.chat_message("assistant"):
                completion = client.chat.completions.create(
                    model=selected_brain,
                    messages=[{"role": "system", "content": "तुम राजाराम भाई की AI हो। हिंदी में छोटा और शाही जवाब दो।"}] + 
                             [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                
                ans = completion.choices[0].message.content
                st.markdown(ans)
                st.caption(f"इस्तेमाल किया गया दिमाग: {selected_brain}")
                
                shakti_speak(ans)

            st.session_state.messages.append({"role": "assistant", "content": ans})

        except Exception as e:
            st.error(f"क्षमा करें भाई, इस दिमाग ({selected_brain}) में आज कुछ तकनीकी काम चल रहा है। कृपया फिर से पूछें।")
            # अगर एरर आए तो पुराना मॉडल लिस्ट से हटाना बेहतर है (सिर्फ इस बार के लिए)

if __name__ == "__main__":
    main()
