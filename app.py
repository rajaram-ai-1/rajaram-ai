import streamlit as st
from groq import Groq
import time
import random

# --- 1. शाही डार्क और हैकर लुक ---
st.set_page_config(page_title="RAJARAM-X: THE ULTIMATE ORACLE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; }
    .oracle-card { 
        border: 2px solid #00FF41; padding: 15px; border-radius: 15px; 
        background: rgba(0, 255, 65, 0.05); min-height: 250px;
        box-shadow: 0 0 15px #00FF41; margin-bottom: 20px;
    }
    .status-active { color: #00FF41; font-weight: bold; font-family: 'Courier New'; }
    /* चैट इनपुट को नीचे रखने की कोशिश के लिए स्टाइल */
    .stChatFloatingInputContainer { background-color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 30 शक्तिशाली और चालू दिमागों की फौज (Updated for 2026) ---
# हमने सिर्फ वही रखे हैं जो Groq पर सबसे ज्यादा स्टेबल हैं
MODELS_ARMY = [
    "llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768",
    "gemma2-9b-it", "llama-3.2-11b-vision-preview", "llama-3.2-3b-preview",
    "llama-3.2-1b-preview", "distil-grenache-8b-llama-3.1"
]

def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 RAJARAM-X: MULTIVERSAL COMMAND</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>दुनिया का सबसे शक्तिशाली AI Command Center - इनाम जीतने वाला एडिशन</p>", unsafe_allow_html=True)

    # चैट हिस्ट्री को संभालना
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # पुराने संदेश दिखाना (ऊपर)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- 3. चैटबॉक्स अब नीचे है (st.chat_input का उपयोग) ---
    prompt = st.chat_input("अपना आदेश यहाँ लिखें, राजाराम भाई...")

    if prompt:
        # यूजर का मैसेज दिखाना
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        st.write("---")
        # 3 अलग दृष्टिकोणों के लिए कॉलम
        cols = st.columns(3)
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        
        # इनाम जीतने के लिए 3 अलग काल (Past, Present, Future)
        perspectives = [
            {"label": "📜 इतिहास (Past)", "query": f"इतिहास के संदर्भ में: {prompt}"},
            {"label": "🌍 वर्तमान (Present)", "query": f"वर्तमान स्थिति: {prompt}"},
            {"label": "🚀 भविष्य (Future)", "query": f"भविष्य की भविष्यवाणी (100 साल बाद): {prompt}"}
        ]

        for i, p in enumerate(perspectives):
            with cols[i]:
                st.markdown(f"<div class='oracle-card'>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='color: gold;'>{p['label']}</h3>", unsafe_allow_html=True)
                
                # 'जाम' होने से बचने के लिए रैंडम दिमाग चुनना
                success = False
                random_army = random.sample(MODELS_ARMY, len(MODELS_ARMY))
                
                for brain in random_army:
                    if success: break
                    try:
                        start = time.time()
                        response = client.chat.completions.create(
                            model=brain,
                            messages=[{"role": "system", "content": "तुम राजाराम के महा-द्रष्टा AI हो। हिंदी में शाही जवाब दो।"},
                                     {"role": "user", "content": p['query']}]
                        )
                        end = time.time()
                        
                        st.write(response.choices[0].message.content)
                        st.markdown(f"<p class='status-active'>⚡ दिमाग: {brain} | रफ़्तार: {round(end-start, 3)}s</p>", unsafe_allow_html=True)
                        success = True
                    except:
                        continue # अगर एक दिमाग जाम है, तो अगले पर जाओ
                
                if not success:
                    st.error("सभी दिमाग अभी ध्यान में हैं।")
                
                st.markdown("</div>", unsafe_allow_html=True)

        # AI का मुख्य जवाब हिस्ट्री में जोड़ना (Present वाला)
        # यहाँ आप चाहें तो और लॉजिक जोड़ सकते हैं

if __name__ == "__main__":
    main()
        
