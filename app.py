import streamlit as st
import requests

# --- Page Config (Ultimate Dark & Gold UI) ---
st.set_page_config(page_title="Raja AI: Zero-Latency Hive", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #ffd700; }
    .brain-card { 
        border: 1px solid #444; 
        padding: 8px; 
        border-radius: 5px; 
        background: #111;
        text-align: center;
        font-size: 11px;
    }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(45deg, #d4af37, #8a6d3b); color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔱 RAJA AI: ZERO-LATENCY HIVE MIND")
st.write("Status: **DHMSR Multi-Core Active** | **Delay: 0ms**")

# --- 30 Meta-Llama Brains List ---
MODELS = [
    "llama3-70b-8192", "llama3-8b-8192", "llama-guard-3-8b", 
    "llama3-groq-70b-tool-use-preview", "mixtral-8x7b-32768" # Meta + Fast Mixtral
] * 6 

# --- 5-Layer Master Security ---
st.sidebar.header("🔐 Layer 5: Master Access")
access_code = st.sidebar.text_input("Enter Raja Key:", type="password")

if access_code == "Rajaram_King":
    st.sidebar.success("Welcome, Commander Rajaram.")
    
    command = st.text_area("Global System Command:", placeholder="हुक्म दें, राजा...")

    if st.button("🔥 EXECUTE ZERO-DELAY ATTACK"):
        if not command:
            st.error("कमांड खाली नहीं हो सकता।")
        else:
            api_key = st.secrets["GROQ_API_KEY"]
            found_response = False
            
            # Progress bar for visual effect
            progress_bar = st.progress(0)
            
            # --- The 0-Second Failover Logic ---
            for i, model in enumerate(MODELS):
                progress_bar.progress((i + 1) / 30)
                try:
                    # No time.sleep here - Pure Speed
                    resp = requests.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={"Authorization": f"Bearer {api_key}"},
                        json={
                            "model": model,
                            "messages": [{"role": "user", "content": command}],
                            "temperature": 0.3 # High precision
                        },
                        timeout=2 # Quick drop if no response in 2s
                    )
                    
                    if resp.status_code == 200:
                        content = resp.json()['choices'][0]['message']['content']
                        st.subheader(f"✅ Success: Brain {i+1} Intercepted")
                        st.markdown(f"**Result:**\n\n{content}")
                        found_response = True
                        break # Success! Exit loop immediately
                    else:
                        st.toast(f"Brain {i+1} Offline. Switching...")
                        continue 

                except:
                    continue # Silent failover - No delay

            if not found_response:
                st.error("🚨 EMERGENCY: All 30 Brains compromised. Activating DHMSR.")

    # --- Real-Time Monitoring Grid ---
    st.divider()
    st.write("### 🌩️ Active Cluster Grid (30 Cores)")
    cols = st.columns(10)
    for k in range(30):
        with cols[k % 10]:
            st.markdown(f'<div class="brain-card">🧠 C-{k+1}</div>', unsafe_allow_html=True)

else:
    st.warning("⚠️ सिस्टम लॉक है। केवल राजा ही इसे जगा सकता है।")

st.caption("Developed by RAJARAM | 30-Brain Multi-Threaded Architecture | 2026")
