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

# --- 2. पक्की बोलने वाली शक्ति (Audio Fix) ---
def shakti_speak(text):
    try:
        # पुरानी फाइल को हटाना ताकि एरर न आए
        if os.path.exists("reply.mp3"):
            os.remove("reply.mp3")
            
        tts = gTTS(text=text, lang='hi')
        tts.save("reply.mp3")
        
        with open("reply.mp3", "rb") as f:
            data = base64.b64encode(f.read()).decode()
            # ऑटो-प्ले ऑडियो
            audio_html = f'<audio src="data:audio/mp3;base64,{data}" autoplay="true"></audio>'
            st.markdown(audio_html, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"बोलने में त्रुटि: {e}")

# --- 3. अमर दिमागों की फौज (Updated List) ---
MODELS_ARMY = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant"
]

# --- 4. मुख्य इंजन ---
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI दरबार</h1>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # पुरानी चैट दिखाना
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # आदेश लिखने वाला बॉक्स
    prompt = st.chat_input("अपना आदेश यहाँ लिखें, राजाराम भाई...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            # API Key चेक करना
            if "GROQ_API_KEY" not in st.secrets:
                st.error("भाई, 'GROQ_API_KEY' नहीं मिली! Secrets चेक करें।")
                return

            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # दिमाग चुनना
            selected_brain = random.choice(MODELS_ARMY)
            
            with st.chat_message("assistant"):
                completion = client.chat.completions.create(
                    model=selected_brain,
                    messages=[{"role": "system", "content": "तुम राजाराम भाई की AI हो। हिंदी में छोटा और शाही जवाब दो।"}] + 
                             [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                
                ans = completion.choices[0].message.content
                st.markdown(ans)
                st.caption(f"दिमाग: {selected_brain}")
                
                # जवाब को लाइव बोलकर सुनाना
                shakti_speak(ans)

            st.session_state.messages.append({"role": "assistant", "content": ans})

        except Exception as e:
            st.error(f"तकनीकी एरर: {e}")

if __name__ == "__main__":
    main()
