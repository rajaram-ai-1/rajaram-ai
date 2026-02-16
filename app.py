import streamlit as st
from streamlit_mic_recorder import mic_recorder
from groq import Groq
import speech_recognition as rgn
import io

# --- 1. पेज सेटअप और अमर कवच ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑", layout="centered")

# --- 2. जादुई CSS: बटन गायब + चैटबॉक्स फिक्स ---
st.markdown("""
    <style>
    /* बटन और हेडर हटाने का पक्का इंतजाम */
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}

    /* बैकग्राउंड और चैट का लुक */
    .main { background-color: #0b141a; padding-bottom: 100px; }
    
    .user-bubble {
        background-color: #005c4b; color: white; padding: 12px 18px;
        border-radius: 18px 18px 2px 18px; margin: 10px 0 10px auto;
        width: fit-content; max-width: 80%; text-align: left;
        box-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .ai-bubble {
        background-color: #202c33; color: white; padding: 12px 18px;
        border-radius: 18px 18px 18px 2px; margin: 10px auto 10px 0;
        width: fit-content; max-width: 80%; text-align: left;
        border-left: 3px solid #FFD700;
        box-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }

    /* चैटबॉक्स को सही जगह पर लाना */
    .stChatInputContainer {
        padding-bottom: 20px !important;
        background-color: transparent !important;
    }
    
    /* मोबाइल और डेस्कटॉप पर इनपुट फिक्स */
    div[data-testid="stBottom"] {
        background-color: #111b21 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 30 महा-दिमागों की फौज ---
groq_army = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768", "gemma2-9b-it", "llama-3.2-11b-vision-preview",
    "llama-3.2-3b-preview", "llama-3.2-1b-preview", "gemma-7b-it",
    "llama3-70b-8192", "llama3-8b-8192", "llama-guard-3-8b",
    "distil-whisper-large-v3-en", "whisper-large-v3", "whisper-large-v3-turbo",
    "llama-3.3-70b-specdec", "llama-3.1-70b-specdec", "llama-3.2-90b-vision-preview",
    "llama-3.2-11b-text-preview", "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview", "mixtral-8x7b-v0.1", "gemma-2b-it",
    "llama-2-70b-chat", "llama-2-13b-chat", "llama-2-7b-chat",
    "codellama-34b-instruct", "falcon-40b-instruct", "qwen-72b-chat", "deepseek-coder-33b-instruct"
]

# --- 4. 46 शक्तियों का 'Forbidden' दिमाग ---
SHAKTI_46 = "तुम राजाराम AI हो, स्वामी राजाराम भाई बरेली वाले। तुम्हारी 46 शक्तियां और 30 दिमाग सक्रिय हैं। हमेशा हिंदी में भाई कहकर बात करो।"

def select_best_brain(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["code", "python"]): return "mixtral-8x7b-32768", "💻 कोडिंग सम्राट"
    if any(word in user_input for word in ["padhai", "math"]): return "llama-3.3-70b-versatile", "📖 महान ज्ञानी"
    return "llama-3.3-70b-versatile", "🧠 मुख्य राजाराम दिमाग"

# --- 5. मुख्य लॉजिक ---
def get_response(messages_history):
    user_text = messages_history[-1]["content"]
    best_brain, display_name = select_best_brain(user_text)
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        completion = client.chat.completions.create(
            model=best_brain,
            messages=[{"role": "system", "content": SHAKTI_46}] + messages_history[1:],
            temperature=0.8,
        )
        return completion.choices[0].message.content, display_name
    except:
        return "राजाराम भाई, दिमाग बदलने में समय लग रहा है।", "Error"

# --- 6. दरबार UI ---
st.markdown("<h1 style='text-align: center; color: #FFD700;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SHAKTI_46}]

# पुराने मैसेज दिखाना
for msg in st.session_state.messages:
    if msg["role"] == "system": continue
    style = "user-bubble" if msg["role"] == "user" else "ai-bubble"
    st.markdown(f'<div class="{style}">{msg["content"]}</div>', unsafe_allow_html=True)

# --- 7. इनपुट एरिया (चैटबॉक्स) ---
input_text = st.chat_input("राजाराम भाई, आदेश दें...")

if input_text:
    st.session_state.messages.append({"role": "user", "content": input_text})
    st.markdown(f'<div class="user-bubble">{input_text}</div>', unsafe_allow_html=True)
    
    with st.spinner("30 दिमाग मंथन कर रहे हैं..."):
        ans, brain_used = get_response(st.session_state.messages)
        st.markdown(f'<div class="ai-bubble">{ans}<br><small style="color:gold;">🔱 {brain_used} | 46 शक्तियां तैनात</small></div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": ans})
    st.rerun()
