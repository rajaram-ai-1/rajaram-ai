import streamlit as st
from groq import Groq
import base64

# --- 1. सुरक्षा कवच ---
try:
    # अब सिर्फ एक ही चाबी की जरूरत है
    GROQ_K = st.secrets["GROQ_API_KEY"]
    client_groq = Groq(api_key=GROQ_K)
except:
    st.error("भाई, Secrets में GROQ_API_KEY चेक करो!")
    st.stop()

# --- 2. Groq का 'देखने' वाला दिमाग ---
def get_groq_vision_response(text, file):
    try:
        # फोटो को बाइनरी में बदलना
        image_data = base64.b64encode(file.read()).decode('utf-8')
        
        # Groq का विजन मॉडल इस्तेमाल करना
        completion = client_groq.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text if text else "इस फोटो को समझाओ भाई"},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
                        },
                    ],
                }
            ],
            temperature=0.7,
        )
        return completion.choices[0].message.content, "Groq Vision 📷"
    except Exception as e:
        return f"भाई, ग्रॉक भी थक गया है: {str(e)}", "Error"

# --- 3. इंटरफ़ेस (Gemini 3 Style) ---
st.set_page_config(page_title="Rajaram AI", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: #131314; color: white; }
    .chat-bubble { padding: 15px; border-radius: 15px; border: 1px solid #3c3f43; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 Rajaram AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# चैट दिखाना
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- 4. टूल्स और चैट बॉक्स ---
col1, col2 = st.columns([1, 5])
with col1:
    up_file = st.file_uploader("📷", type=['png', 'jpg', 'jpeg'], key="cam", label_visibility="collapsed")

with col2:
    prompt = st.chat_input("अब गूगल का डर नहीं, पूछो भाई...")

if prompt or up_file:
    user_txt = prompt if prompt else "फोटो देखो भाई"
    
    if not st.session_state.messages or st.session_state.messages[-1]["content"] != user_txt:
        st.session_state.messages.append({"role": "user", "content": user_txt})
        with st.chat_message("user"):
            st.write(user_txt)
            if up_file: st.image(up_file, width=200)

        with st.spinner("राजाराम AI की विजन शक्ति काम कर रही है..."):
            if up_file:
                ans, brain = get_groq_vision_response(user_txt, up_file)
            else:
                # नॉर्मल चैट के लिए 70B वाला बड़ा दिमाग
                res = client_groq.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": user_txt}]
                )
                ans, brain = res.choices[0].message.content, "Llama 3.3 ⚡"
            
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.write(ans)
                st.caption(f"Active Power: {brain}")
