import streamlit as st
from groq import Groq

# 1. पेज सेटिंग (यह सबसे ऊपर ही होनी चाहिए)
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# 2. सुरक्षा कवच (बटन्स और हेडर गायब करने के लिए)
st.markdown("""
    <style>
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    #MainMenu {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# 3. तिजोरी से चाबी निकालना
try:
    if "GROQ_API_KEY" in st.secrets:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    else:
        st.error("❌ भाई, Secrets में 'GROQ_API_KEY' नहीं मिली!")
        st.stop()
except Exception as e:
    st.error(f"❌ कनेक्शन एरर: {e}")
    st.stop()

# 4. 25+ शक्तिशाली दिमागों की महा-फौज
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it",
    "llama-guard-3-8b", "distil-whisper-large-v3-en"
]

def get_response(messages_history):
    for brain in groq_army:
        try:
            completion = client.chat.completions.create(
                model=brain,
                messages=messages_history,
                temperature=0.7,
                max_tokens=2048,
            )
            return completion.choices[0].message.content, brain
        except:
            continue
    return "भाई, फौज अभी विश्राम पर है।", "None"

# 5. दरबार की सजावट
st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25+ महा-शक्तियों का कवच  -  अमर और सुरक्षित</b></p>", unsafe_allow_html=True)

# 6. याददाश्त
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम 'राजाराम AI' हो। और यह आपके लिए बरेली के राजाराम भाई ने बनाया है जो 15 साल के क्लास 10 के स्टूडेंट हैं, वे बहुत इंटेलिजेंट हैं। यूज़र को हमेशा बैलेंस्ड जवाब दें, न बहुत लंबा और न बहुत छोटा।हमेशा हिंदी में बात करो और 'भाई' कहकर सम्मान दो।"}
    ]

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 7. हुक्म और जवाब
prompt = st.chat_input("हुक्म करें राजाराम भाई...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("फौज मोर्चा संभाल रही है..."):
        answer, used_id = get_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
            st.caption(f"सक्रिय शक्ति: {used_id}")
        st.rerun()
