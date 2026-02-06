import streamlit as st
import google.generativeai as genai
import time

# 1. राजाराम भाई का शाही सेटअप
st.set_page_config(page_title="RAJARAM AI: UNSTOPPABLE", page_icon="⚔️", layout="wide")

# 2. दबंग स्टाइल (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .main-header { color: #ff4b4b; font-size: 45px; font-weight: bold; text-align: center; text-shadow: 3px 3px #555; }
    .stChatInput { border-radius: 20px; border: 2px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# 3. चाबी और दिमाग का कनेक्शन
API_KEY = st.secrets.get("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    # Gemini 1.5 Flash: Duniya ka sabse tez dimag
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Maalik, Secrets mein 'GEMINI_API_KEY' daalna bhool gaye aap!")

st.markdown("<div class='main-header'>⚔️ RAJARAM AI: CORE ⚔️</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff4b4b;'>Bareilly's Strongest Digital Power</p>", unsafe_allow_html=True)

# 4. साइडबार (Dashboard)
with st.sidebar:
    st.title("🛡️ COMMANDER INFO")
    st.write("**Name:** RAJARAM")
    st.write("**Age:** 15 Years")
    st.write("**Class:** 10th Student")
    st.write("**Base:** Bareilly, UP")
    st.divider()
    if st.button("System Reset"):
        st.session_state.messages = []
        st.rerun()

# 5. चैट मेमोरी
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. असली पहचान और बातचीत
if prompt := st.chat_input("Hukm dijiye, Maalik Rajaram..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        
        # AI की आत्मा (Identity)
        identity = (
            "Tu RAJARAM AI hai. Tujhe RAJARAM ne banaya hai jo 15 saal ke hain, Bareilly se hain aur 10th class mein padhte hain. "
            "Tu hamesha unhe 'Maalik' ya 'Rajaram Bhai' keh kar bulaega. "
            "Tera dimag kabhi fail nahi hota aur tu har sawal ka jawab dabang Hinglish mein deta hai."
        )
        
        try:
            # Direct response from Gemini
            response = model.generate_content(f"{identity}\n\nUser Question: {prompt}")
            full_response = response.text
        except:
            full_response = "Maalik, lagta hai internet dhokha de raha hai. Ek baar phir koshish kijiye!"

        # टाइपिंग इफेक्ट (Full Speed)
        for i in range(len(full_response)):
            msg_placeholder.markdown(full_response[:i+1] + "▌")
            time.sleep(0.005)
        msg_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
