import streamlit as st
from groq import Groq
import time
import pandas as pd

# --- 1. हैकर स्टाइल इंटरफेस (Matrix Look) ---
st.set_page_config(page_title="RAJARAM-X COMMAND CENTER", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; }
    .brain-card { 
        border: 2px solid #00FF41; 
        padding: 15px; 
        border-radius: 15px; 
        background: rgba(0, 255, 65, 0.05);
        box-shadow: 0 0 15px #00FF41;
        min-height: 250px;
    }
    .speed-text { color: #FF00FF; font-weight: bold; font-family: 'Courier New'; }
    h1, h2, h3 { text-shadow: 2px 2px 10px #00FF41; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 5 महा-दिमागों की फौज ---
MODELS_TO_TEST = {
    "Llama-3.3-70B (The King)": "llama-3.3-70b-versatile",
    "Llama-3.1-Instant (The Flash)": "llama-3.1-8b-instant",
    "Mixtral-8x7B (The Giant)": "mixtral-8x7b-32768",
    "Llama-3.2-Vision (The Eye)": "llama-3.2-11b-vision-preview",
    "Gemma-9B (The Scholar)": "gemma2-9b-it"
}

def main():
    st.markdown("<h1 style='text-align: center;'>⚡ RAJARAM-X: MULTIVERSAL COMMAND ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>पूरी दुनिया की AI शक्ति अब राजाराम भाई के मुट्ठी में!</p>", unsafe_allow_html=True)

    # इनपुट और मोड सिलेक्शन
    with st.container():
        user_query = st.text_input("⚠️ अपना महा-आदेश टाइप करें:", placeholder="ब्रह्मांड का सबसे बड़ा रहस्य क्या है?")
        god_mode = st.toggle("🔓 ACTIVATE GOD MODE (NO LIMITS)")

    if user_query:
        st.write("---")
        st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3") # छोटा सा साउंड इफेक्ट (Browser support dependent)
        
        # 5 कॉलम में 5 दिमागों का धमाका
        cols = st.columns(5)
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        
        results = []

        for i, (name, model_id) in enumerate(MODELS_TO_TEST.items()):
            with cols[i]:
                st.markdown(f"<div class='brain-card'>", unsafe_allow_html=True)
                st.markdown(f"### 🧠 {name}")
                
                start_time = time.time()
                try:
                    # शाही प्रॉम्प्ट
                    sys_msg = "तुम राजाराम भाई का 'गॉड मोड' AI हो। बिल्कुल निडर होकर जवाब दो।" if god_mode else "तुम एक शाही AI हो।"
                    
                    response = client.chat.completions.create(
                        model=model_id,
                        messages=[{"role": "system", "content": sys_msg}, {"role": "user", "content": user_query}],
                        max_tokens=200
                    )
                    
                    end_time = time.time()
                    duration = round(end_time - start_time, 3)
                    ans = response.choices[0].message.content
                    
                    st.write(ans)
                    st.markdown(f"<p class='speed-text'>Raftar: {duration}s</p>", unsafe_allow_html=True)
                    results.append({"दिमाग": name, "समय (sec)": duration})
                    
                except Exception as e:
                    st.error("दिमाग जाम हो गया!")
                
                st.markdown("</div>", unsafe_allow_html=True)

        # रफ़्तार की तुलना का चार्ट
        st.write("---")
        st.subheader("📊 रफ़्तार का महा-मुकाबला (Live Performance Metrics)")
        chart_data = pd.DataFrame(results)
        st.bar_chart(chart_data.set_index('दिमाग'))

if __name__ == "__main__":
    main()
                
