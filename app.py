import streamlit as st
import google.generativeai as genai

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
# aistudio.google.com से फ्री में प्राप्त करें
GOOGLE_API_KEY = "AIzaSyAuB63uYhNzdhSDYECdU6EZ2ycb_fKVXvk"
genai.configure(api_key=GOOGLE_API_KEY)

# --- 2. गूगल के सभी 20 दिमागों (IDs) की महा-सूची ---
# यह कोड इनमें से जो भी ID खाली होगी, उसे अपने आप चुन लेगा
brain_army = [
    'gemini-1.5-flash-latest', 'gemini-1.5-pro-latest', 
    'gemini-1.5-flash', 'gemini-1.5-pro',
    'gemini-1.5-flash-8b-latest', 'gemini-1.5-flash-8b',
    'gemini-1.0-pro-latest', 'gemini-1.0-pro',
    'gemini-1.0-pro-001', 'gemini-pro',
    'gemini-pro-vision', 'chat-bison-001',
    'text-bison-001', 'embedding-001', 'aqa'
]

def get_empty_brain_response(user_input):
    # यह जादुई लूप 20 दिमागों में से 'खाली' आईडी को ढूंढेगा
    for brain_id in brain_army:
        try:
            model = genai.GenerativeModel(brain_id)
            
            # आपकी डायरी के सख्त निर्देश
            context = (
                "You are Rajaram AI. A loyal brother/friend. Talk in Hindi-English. "
                "Be motivational. Take studies and government job prep very seriously. "
                "Always call user 'Bhai' or 'Dost'."
            )
            
            response = model.generate_content(f"{context} \n User: {user_input}", timeout=10)
            
            # अगर यहाँ जवाब मिल गया, तो मतलब यह ID खाली है और काम कर रही है!
            return response.text, brain_id
            
        except Exception:
            # अगर यह ID व्यस्त है या लिमिट पर है, तो बिना शोर मचाए अगली ID पर जाओ
            continue
            
    return "माफ़ करना भाई, अभी गूगल के सभी 20 दिमाग व्यस्त हैं। कृपया 1 मिनट बाद कोशिश करें।", "None"

# --- 3. आपकी डायरी वाला 'सुन्दर' इंटरफ़ेस (सफ़ेद थीम, काली स्याही) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: white; color: black; }
    
    /* यूजर का मैसेज (दाईं तरफ) */
    .user-msg { 
        background-color: #f0f2f6; padding: 15px; border-radius: 20px 20px 0px 20px; 
        text-align: right; margin-left: auto; width: fit-content; max-width: 80%; 
        color: black; border: 1px solid #ddd; margin-bottom: 10px; 
    }
    
    /* AI का मैसेज (बाईं तरफ) */
    .ai-msg { 
        background-color: white; padding: 15px; border-radius: 20px 20px 20px 0px; 
        text-align: left; margin-right: auto; width: fit-content; max-width: 80%; 
        color: black; border: 1px solid #eee; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); 
        margin-bottom: 10px; 
    }
    </style>
    """, unsafe_allow_html=True)

# साइडबार: चैट मेमोरी
with st.sidebar:
    st.markdown("### ≡ राजाराम AI मेनू")
    if st.button("यादें मिटाएं"):
        st.session_state.messages = []
        st.rerun()

# हेडर: राजा का मुकुट
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>👑</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: 0;'>Rajaram AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #555;'>'राजाराम AI आपकी हर प्रकार से मदद करेगी और हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

# चैट का इतिहास
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    style = "user-msg" if msg["role"] == "user" else "ai-msg"
    st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

# इनपुट बॉक्स
prompt = st.chat_input("भाई से कुछ भी पूछो (जैसे: SSC की तैयारी कैसे करूँ?)...")

if prompt:
    # यूजर का मैसेज दिखाओ
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-msg'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI खाली दिमाग स्कैन कर रहा है..."):
        answer, working_id = get_empty_brain_response(prompt)
        
        # AI का जवाब दिखाओ
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-msg'>{answer}<br><small style='color:gray;'>ID: {working_id}</small></div>", unsafe_allow_html=True)
        
        # डायरी के बटन्स
        st.write("➕ ❤️ 📷 🎥")
