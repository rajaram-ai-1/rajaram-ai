import streamlit as st
import google.generativeai as genai

# --- 1. अपनी गूगल मास्टर चाबी यहाँ डालें ---
# aistudio.google.com से प्राप्त करें
GOOGLE_API_KEY = "AIzaSyCEaasqfKx3uMBIReMj4FuQyk-OWxpW99Y"
genai.configure(api_key=GOOGLE_API_KEY)

# --- 2. गूगल के 20 दिमागों (IDs) की सेना ---
brain_army = [
    'gemini-1.5-flash-latest', 'gemini-1.5-pro-latest', 
    'gemini-1.5-flash', 'gemini-1.5-pro',
    'gemini-1.5-flash-8b-latest', 'gemini-1.5-flash-8b',
    'gemini-1.0-pro-latest', 'gemini-1.0-pro',
    'gemini-1.0-pro-001', 'gemini-pro',
    'chat-bison-001', 'text-bison-001'
]

def get_empty_brain_response(user_input):
    # यह लूप हर आईडी को चेक करेगा
    for brain_id in brain_army:
        try:
            model = genai.GenerativeModel(brain_id)
            
            # आपकी डायरी के निर्देश: भाई, दोस्त और पढ़ाई का मार्गदर्शक
            context = (
                "You are Rajaram AI. A loyal brother/friend. Talk in Hindi-English. "
                "Be motivational. Take studies and government job prep very seriously. "
                "Always call user 'Bhai' or 'Dost'."
            )
            
            response = model.generate_content(f"{context} \n User: {user_input}", timeout=10)
            
            # अगर जवाब मिल गया, तो लौट जाओ
            return response.text, brain_id
            
        except Exception as e:
            # --- जासूसी लाइन: यह बताएगी कि गड़बड़ कहाँ है ---
            st.warning(f"ID {brain_id} में हलचल है: {str(e)}")
            continue
            
    return "माफ़ करना भाई, गूगल के सभी दिमाग अभी थके हुए हैं।", "None"

# --- 3. राजाराम AI का सुंदर इंटरफ़ेस (सफ़ेद थीम) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    /* सफ़ेद बैकग्राउंड और काली स्याही */
    .stApp { background-color: white; color: black; }
    
    /* यूजर का मैसेज */
    .user-msg { 
        background-color: #f0f2f6; padding: 15px; border-radius: 20px 20px 0px 20px; 
        text-align: right; margin-left: auto; width: fit-content; max-width: 80%; 
        color: black; border: 1px solid #ddd; margin-bottom: 10px; 
    }
    
    /* AI का मैसेज */
    .ai-msg { 
        background-color: white; padding: 15px; border-radius: 20px 20px 20px 0px; 
        text-align: left; margin-right: auto; width: fit-content; max-width: 80%; 
        color: black; border: 1px solid #eee; box-shadow: 2px 2px 8px rgba(0,0,0,0.05); 
        margin-bottom: 10px; 
    }
    </style>
    """, unsafe_allow_html=True)

# साइडबार: यादें
with st.sidebar:
    st.markdown("### ≡ राजाराम AI")
    if st.button("चैट मेमोरी साफ़ करें"):
        st.session_state.messages = []
        st.rerun()

# हेडर: मुकुट और राजाराम संदेश
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>👑</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-top: 0;'>Rajaram AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>'राजाराम AI आपकी मदद के लिए हमेशा आपके साथ है'</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# पुराना इतिहास दिखाना
for msg in st.session_state.messages:
    style = "user-msg" if msg["role"] == "user" else "ai-msg"
    st.markdown(f"<div class='{style}'>{msg['content']}</div>", unsafe_allow_html=True)

# इनपुट बॉक्स
prompt = st.chat_input("भाई से कुछ भी पूछो...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-msg'>{prompt}</div>", unsafe_allow_html=True)

    with st.spinner("राजाराम AI खाली आईडी ढूंढ रहा है..."):
        answer, used_id = get_empty_brain_response(prompt)
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='ai-msg'>{answer}<br><small style='color:gray;'>कामयाब ID: {used_id}</small></div>", unsafe_allow_html=True)
        
        # डायरी के बटन्स
        st.write("➕ ❤️ 📷 🎥")
