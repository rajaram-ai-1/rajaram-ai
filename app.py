import streamlit as st
import base64  # यह फोटो को कोड में बदलने के लिए है
from PIL import Image
from groq import Groq

# 1. पेज सेटिंग (सबसे ऊपर)
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- राजाराम भाई का 'दिमाग' चुनने वाला इंजन (नया जोड़ा गया) ---
def select_best_brain(messages_history):
    user_input = messages_history[-1]["content"].lower()
    if any(word in user_input for word in ["padhai", "maths", "science", "exam", "book", "class", "study"]):
        return "llama-3.3-70b-versatile", "📖 पढ़ाई वाला दिमाग (Llama 70B)"
    elif any(word in user_input for word in ["majak", "joke", "funny", "hi", "hello", "kaise ho"]):
        return "llama-3.1-8b-instant", "😂 चुलबुला दिमाग (Llama 8B)"
    else:
        return "llama-3.3-70b-versatile", "🧠 ज्ञानी दिमाग (Mixtral)"

# 2. सुरक्षा कवच (स्टाइलिंग)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    div[data-testid="stStatusWidget"] {display:none !important;}
    button[title="Manage app"] {display: none !important;}
    .viewerBadge_container__1QS13 {display: none !important;}
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

# 4. 25+ शक्तिशाली दिमागों की महा-फौज (आपकी लिस्ट सुरक्षित है)
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", 
    "llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview",
    "llama-3.1-8b-instant", "llama3-70b-8192", 
    "llama3-8b-8192", "mixtral-8x7b-32768", 
    "gemma2-9b-it", "gemma-7b-it",
    "llama-guard-3-8b", "distil-whisper-large-v3-en"
]

# 5. रिस्पॉन्स फंक्शन (इसे मैंने आपके पुराने कोड में फिट कर दिया है)
def get_response(messages_history):
    # स्मार्ट तरीके से दिमाग चुनना
    best_brain, brain_display_name = select_best_brain(messages_history)
    
    try:
        completion = client.chat.completions.create(
            model=best_brain,
            messages=messages_history,
            temperature=0.7,
            max_tokens=2048,
        )
        return completion.choices[0].message.content, brain_display_name
    except Exception as e:
        return f"माफ़ करना भाई, गड़बड़ हो गई: {e}", "Error"
def get_meta_vision_response(user_prompt, image_file): 
         (
    )
# 6. दरबार की सजावट
st.markdown("<h1 style='text-align: center;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>25+ महा-शक्तियों का कवच - अमर ,सुरक्षित और तेज़</b></p>", unsafe_allow_html=True)

# 7. याददाश्त
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "तुम 'राजाराम AI' हो। और यह आपके लिए बरेली के राजाराम भाई ने बनाया है जो 15 साल के क्लास 10 के स्टूडेंट हैं, वे बहुत इंटेलिजेंट हैं।आपको पढ़ाई को गंभीरता से लेना चाहिए। अगर कोई कहे कि मुझे इस क्लास के इस सब्जेक्ट की तैयारी कराओ, तो उसे टीचर की तरह समझाओ। हमेशा हिंदी में बात करो और 'भाई' कहकर सम्मान दो।"}
    ]

# पुरानी चैट दिखाना
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
# --- यहाँ से नया कोड शुरू (इसे 'for' लूप के ठीक नीचे पेस्ट करें) ---
# 1. CSS का महा-जादू (यह चैटबॉक्स को असली Gemini जैसा बनाएगा)
st.markdown("""
<style>
    /* पूरे बॉक्स को घेरने वाला कंटेनर */
    .main-input-container {
        position: fixed;
        bottom: 30px;
        width: 70%;
        background: #202123;
        border: 1px solid #4d4d4d;
        border-radius: 25px;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        z-index: 9999;
    }
    /* फ़ाइल अपलोडर को छिपाना और सिर्फ आइकन दिखाना */
    .stFileUploader {
        width: 40px;
        overflow: hidden;
    }
    .stFileUploader section {
        padding: 0 !important;
        border: none !important;
        background: transparent !important;
    }
    div[data-testid="stFileUploader"] label, div[data-testid="stFileUploader"] small {
        display: none !important;
    }
    /* प्लस बटन को प्लस जैसा दिखाना */
    .stFileUploader span::before {
        content: '➕';
        font-size: 20px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# 2. असली लेआउट
col1, col2 = st.columns([1, 10])

with col1:
    # यह आपका जादुई प्लस बटन है
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], key="final_plus")

with col2:
    # यह आपका टाइपिंग एरिया
    prompt = st.chat_input("हुक्म करें राजाराम भाई...")

# 3. जवाब न आने वाली समस्या का समाधान (Logic)
if prompt:
    # यूजर का मैसेज दिखाएं
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # असली चेक: फोटो और टेक्स्ट दोनों साथ भेज रहे हैं या नहीं
    if uploaded_file is not None:
        with st.spinner("राजाराम AI आपकी फोटो देख रहा है..."):
            # यहाँ आपका विजन फंक्शन कॉल होगा
            answer = get_meta_vision_response(prompt, uploaded_file)
    else:
        with st.spinner("राजाराम AI गहराई से सोच रहा है..."):
            # सिर्फ टेक्स्ट वाला जवाब
            answer, used_id = get_response(st.session_state.messages)

    # AI का जवाब स्क्रीन पर लाना
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
    
    st.rerun()
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("फौज मोर्चा संभाल रही है..."):
        # यहाँ आपका 'answer' और 'used_id' सही से सेट हो गया है
        answer, used_id = get_response(st.session_state.messages)
        st.toast(f"अभी {used_id} एक्टिव है!", icon='🔥')
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
            st.caption(f"सक्रिय शक्ति: {used_id}")
        
        st.rerun()
