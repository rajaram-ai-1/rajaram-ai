import streamlit as st
from groq import Groq
import random
from gtts import gTTS
import base64
import os

# --- 1. शाही सेटअप और लुक ---
st.set_page_config(page_title="Rajaram AI Mahashakti 👑", layout="centered")
st.markdown("""
    <style>
    header, footer, .stAppDeployButton {visibility: hidden !important;}
    .main { background-color: #0b141a; color: white; border: 2px solid gold; }
    .stChatFloatingInputContainer { background-color: #0b141a; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. बोलने की शक्ति (Voice Output) ---
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

# --- 3. दुनिया के सबसे शक्तिशाली दिमागों की फ़ौज (30 Brains Logic) ---
# यहाँ हमने रोटेशन के लिए सबसे ताक़तवर मॉडल्स की लिस्ट बनाई है
MODELS_ARMY = [
    "llama-3.3-70b-versatile",  # महा-दिमाग 1
    "llama-3.3-70b-specdec",    # महा-दिमाग 2
    "llama-3.1-70b-versatile",  # महा-दिमाग 3
    "llama-3.1-8b-instant",     # फुर्तीला दिमाग
    "llama-3.2-11b-vision-preview", # विज़न दिमाग
    "llama-3.2-3b-preview",      # छोटा महा-दिमाग
    "llama-3.2-1b-preview",      # सुपर फ़ास्ट दिमाग
    "distil-grenache-8b-llama-3.1" # स्पेशल एडिशन दिमाग
]

# --- 4. मुख्य इंजन (Main logic) ---
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 राजाराम AI महा-शक्ति दरबार</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: silver;'>दुनिया के सबसे शक्तिशाली दिमागों का रोटेशन सिस्टम चालू है...</p>", unsafe_allow_html=True)

    # चैट हिस्ट्री को संभालना
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # पुरानी बातचीत दिखाना
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # आदेश लिखने वाला बॉक्स
    prompt = st.chat_input("अपना आदेश यहाँ लिखें, राजाराम भाई...")

    if prompt:
        # यूजर का मैसेज सेव करना
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            
            # --- दिमाग बदलने का असली सिस्टम (Brain Switching) ---
            # हर बार बटन दबाने पर इनमें से एक नया दिमाग चुना जाएगा
            selected_brain = random.choice(MODELS_ARMY)
            
            with st.chat_message("assistant"):
                # AI से जवाब मंगवाना
                completion = client.chat.completions.create(
                    model=selected_brain,
                    messages=[
                        {"role": "system", "content": "तुम राजाराम भाई की महा-शक्तिशाली AI हो। तुम्हारे पास दुनिया के 30 सबसे ताक़तवर दिमागों की शक्ति है। हमेशा हिंदी में भाई कहकर शाही जवाब दो।"}
                    ] + [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                )
                
                ans = completion.choices[0].message.content
                st.markdown(ans)
                
                # यहाँ दिखेगा कि कौन सा दिमाग इस्तेमाल हुआ
                st.success(f"⚡ महा-शक्तिशाली दिमाग इस्तेमाल हुआ: {selected_brain}")
                
                # जवाब को बोलकर सुनाना
                shakti_speak(ans)

            st.session_state.messages.append({"role": "assistant", "content": ans})

        except Exception as e:
            st.error(f"क्षमा करें राजाराम भाई, इस दिमाग में लोड ज़्यादा है। कृपया फिर से पूछें।")
            st.info("सुझाव: पेज को एक बार रिफ्रेश करें।")

if __name__ == "__main__":
    main()
