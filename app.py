import streamlit as st
from groq import Groq
import time
import random

# --- 1. हैकर और शाही लुक ---
st.set_page_config(page_title="RAJARAM-X: THE ULTIMATE ORACLE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; }
    .oracle-card { 
        border: 2px solid #00FF41; padding: 15px; border-radius: 15px; 
        background: rgba(0, 255, 65, 0.05); min-height: 280px;
        box-shadow: 0 0 15px #00FF41; margin-bottom: 20px;
    }
    .status-active { color: #00FF41; font-weight: bold; font-family: 'Courier New'; font-size: 0.8rem; }
    /* चैट इनपुट को नीचे रखने के लिए */
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 के सबसे भरोसेमंद दिमाग (जो कभी बंद नहीं होते) ---
MODELS_ARMY = [
    "llama-3.3-70b-versatile", 
    "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
    "llama-3.2-11b-vision-preview"
]

def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 RAJARAM-X: MULTIVERSAL COMMAND</h1>", unsafe_allow_html=True)

    # चैट हिस्ट्री
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # संदेश दिखाना (ऊपर)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- 3. चैटबॉक्स सबसे नीचे ---
    prompt = st.chat_input("हुकुम करें, राजाराम भाई...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        st.write("---")
        cols = st.columns(3)
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        
        # 3 अलग दृष्टिकोण
        perspectives = [
            {"label": "📜 इतिहास (Past)", "query": f"इतिहास के संदर्भ में गहरे शब्द: {prompt}"},
            {"label": "🌍 वर्तमान (Present)", "query": f"आज की हकीकत: {prompt}"},
            {"label": "🚀 भविष्य (Future)", "query": f"आने वाला समय (भविष्यवाणी): {prompt}"}
        ]

        for i, p in enumerate(perspectives):
            with cols[i]:
                st.markdown(f"<div class='oracle-card'>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='color: gold; text-align: center;'>{p['label']}</h3>", unsafe_allow_html=True)
                
                # ऑटो-स्विच सिस्टम (Fail-Safe)
                success = False
                tried_models = random.sample(MODELS_ARMY, len(MODELS_ARMY))
                
                for brain in tried_models:
                    if success: break
                    try:
                        start = time.time()
                        response = client.chat.completions.create(
                            model=brain,
                            messages=[
                                {"role": "system", "content": "तुम राजाराम के महा-द्रष्टा AI हो। शाही हिंदी में छोटा और गहरा जवाब दो।"},
                                {"role": "user", "content": p['query']}
                            ],
                            timeout=10.0 # 10 सेकंड से ज़्यादा इंतज़ार नहीं करेगा
                        )
                        end = time.time()
                        
                        st.write(response.choices[0].message.content)
                        st.markdown(f"<p class='status-active'>⚡ ACTIVE: {brain} | {round(end-start, 2)}s</p>", unsafe_allow_html=True)
                        success = True
                    except:
                        continue # अगर एक दिमाग थका हुआ है, तो तुरंत अगला आ जाएगा
                
                if not success:
                    st.write("⚠️ यह मार्ग अभी धुंधला है, दोबारा प्रयास करें।")
                
                st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
                        
