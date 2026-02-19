import streamlit as st
from groq import Groq
import random
import time

# --- 1. पेज कॉन्फ़िगरेशन ---
st.set_page_config(page_title="RAJARAM-X: THE SUPREME ENGINE", layout="wide")
st.markdown("<style>.stApp { background-color: #0d1117; color: #00FF41; }</style>", unsafe_allow_html=True)

# --- 2. 30 दिमागों का क्लस्टर (Groq Models) ---
# हमने Groq के सबसे ताकतवर मॉडल्स को 30 हिस्सों में बाँटा है
AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768",
    "gemma2-9b-it"
]

# 30 दिमागों का डेटाबेस तैयार करना
if 'brain_cluster' not in st.session_state:
    st.session_state.brain_cluster = {f"Brain-Node-{i}": random.choice(AVAILABLE_MODELS) for i in range(1, 31)}

# --- 3. असली दिमाग का कनेक्शन ---
# अपनी Groq API Key यहाँ डालें
client = Groq(api_key="आपकी_GROQ_API_KEY_यहाँ_डालें")

# --- 4. मुख्य इंटरफ़ेस ---
st.title("👑 RAJARAM-X: 30 BRAINS ACTIVE")

# साइडबार में 30 दिमागों का लाइव स्टेटस
with st.sidebar:
    st.header("🧠 Brain Cluster Status")
    for node, model in st.session_state.brain_cluster.items():
        st.write(f"🟢 {node} ({model})")

# --- 5. असली जवाब देने वाली शक्ति ---
st.subheader("💬 लाइव इंटेलिजेंस (Real AI Response)")
user_query = st.chat_input("हुकुम करें राजाराम भाई, अब असली जवाब आएगा...")

if user_query:
    # 30 में से एक दिमाग को रैंडमली चुनना
    selected_node = random.choice(list(st.session_state.brain_cluster.keys()))
    selected_model = st.session_state.brain_cluster[selected_node]
    
    st.markdown(f"🧠 **आदेश प्राप्त हुआ!** सक्रिय दिमाग: `{selected_node}`")
    
    with st.spinner(f"राजाराम भाई, {selected_node} सोच रहा है..."):
        try:
            # Groq API से असली जवाब मंगवाना
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "तुम राजाराम के महा-शक्तिशाली AI हो। हिंदी में दमदार और शाही जवाब दो।"},
                    {"role": "user", "content": user_query}
                ],
                model=selected_model,
            )
            
            # असली जवाब स्क्रीन पर दिखाना
            response = chat_completion.choices[0].message.content
            st.chat_message("assistant").write(response)
            
        except Exception as e:
            st.error(f"कनेक्शन एरर: {e}")
            st.info("कृपया चेक करें कि आपकी API Key सही है और इंटरनेट चालू है।")

# --- 6. फोटो और आवाज़ की शक्तियाँ ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("🖼️ फोटो निर्माण")
    img_prompt = st.text_input("क्या फोटो बनाऊँ?")
    if st.button("Generate Image"):
        url = f"https://pollinations.ai/p/{img_prompt.replace(' ', '%20')}?width=1024&height=768&model=flux"
        st.image(url, caption=f"Rajaram-X Vision: {img_prompt}")

with col2:
    st.subheader("⚡ सिस्टम स्टेटस")
    st.write("30 दिमाग: **ऑनलाइन**")
    st.write("300 शक्तियाँ: **स्टैंडबाय**")
    if st.button("सिस्टम रिफ्रेश करें"):
        st.rerun()

st.markdown("<p style='text-align: center; color: gray;'>Rajaram-X | World's Most Powerful 30-Brain Cluster</p>", unsafe_allow_html=True)
