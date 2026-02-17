import streamlit as st
from groq import Groq
import time

# --- 1. शाही डार्क इंटरफेस ---
st.set_page_config(page_title="Rajaram Multiversal AI", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; }
    .oracle-card { 
        border: 2px solid #00FF41; padding: 20px; border-radius: 15px; 
        background: rgba(0, 255, 65, 0.05); min-height: 300px;
        box-shadow: 0 0 20px #00FF41;
    }
    .time-label { color: gold; font-weight: bold; font-size: 20px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. सिर्फ सबसे शक्तिशाली और चालू दिमाग ---
# हमने उन मॉडल्स को हटा दिया है जो Error दे रहे थे
POWER_MODELS = [
    "llama-3.3-70b-versatile", # सबसे बड़ा दिमाग
    "llama-3.1-8b-instant",    # सबसे तेज़ दिमाग
    "mixtral-8x7b-32768"       # सबसे गहरा दिमाग
]

def main():
    st.markdown("<h1 style='text-align: center;'>⚡ RAJARAM MULTIVERSAL ORACLE ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>एक सवाल, तीन काल: Groq की असीमित रफ़्तार के साथ</p>", unsafe_allow_html=True)

    # आदेश इनपुट
    user_query = st.text_input("अपना महा-प्रश्न यहाँ दर्ज करें:", placeholder="जैसे: 'इंसान की शक्ति'...")

    if user_query:
        st.write("---")
        cols = st.columns(3)
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        # 3 अलग दृष्टिकोण (Times)
        perspectives = [
            {"time": "भूतकाल (Past)", "prompt": f"इतिहास के नज़रिए से बताओ: {user_query}"},
            {"time": "वर्तमान (Present)", "prompt": f"आज की दुनिया के हिसाब से बताओ: {user_query}"},
            {"time": "भविष्य (Future)", "prompt": f"आने वाले 100 साल बाद क्या होगा: {user_query}"}
        ]

        for i, p in enumerate(perspectives):
            with cols[i]:
                st.markdown(f"<div class='oracle-card'>", unsafe_allow_html=True)
                st.markdown(f"<p class='time-label'>⏳ {p['time']}</p>", unsafe_allow_html=True)
                
                try:
                    start = time.time()
                    # हर कॉलम में अलग मॉडल का इस्तेमाल
                    response = client.chat.completions.create(
                        model=POWER_MODELS[i],
                        messages=[{"role": "system", "content": "तुम राजाराम के महा-द्रष्टा AI हो। हिंदी में शाही जवाब दो।"},
                                 {"role": "user", "content": p['prompt']}]
                    )
                    end = time.time()
                    
                    st.write(response.choices[0].message.content)
                    st.markdown(f"<p style='color: #FF00FF;'>रफ़्तार: {round(end-start, 3)}s</p>", unsafe_allow_html=True)
                except Exception as e:
                    st.error("यह काल अभी बंद है।")
                
                st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
                    
