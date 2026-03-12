import sys
import importlib.util
import datetime
import subprocess
import streamlit as st
import os
import google.generativeai as genai
import time

# --- ०. ब्रह्मांडीय सेटिंग्स (Global Constants) ---
# हमने 'flash-latest' को अपना मुख्य हथियार बना लिया है ताकि 404 न आए
SHAKTI_MODEL = 'gemini-1.5-flash-latest'

def inject_new_shakti(api_key, user_command, power_name):
    """मालिक के हुक्म पर नई फाइल (शक्ति) पैदा करना"""
    try:
        genai.configure(api_key=api_key)
        # यहाँ 'models/' लगाकर साफ़ रास्ता दिया गया है
        shakti_model = genai.GenerativeModel(f'models/{SHAKTI_MODEL}')
        
        prompt = f"Write a standalone Python function 'run_feature()' for: {user_command}. Use streamlit as st. Return ONLY raw code."
        response = shakti_model.generate_content(prompt)
        
        if not response.text:
            return False, "एआई ने कोई जवाब नहीं दिया।"
            
        code = response.text.replace('```python', '').replace('```', '').strip()

        vault_path = "rajaram_vault"
        if not os.path.exists(vault_path):
            os.makedirs(vault_path)
            
        file_path = os.path.join(vault_path, f"feature_{power_name}.py")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("import streamlit as st\nimport os, subprocess\n\n")
            f.write(code)
        
        return True, f"✅ शक्ति '{power_name}' सिद्ध हुई!"
    except Exception as e:
        return False, f"तिजोरी एरर: {str(e)}"

# --- १. महा-शून्य की चाबी (Secrets) ---
api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("gemini_API_key")

if api_key:
    genai.configure(api_key=api_key)
    # 404 फिक्स: यहाँ हमने सीधे 'flash' मॉडल पकड़ा है
    model = genai.GenerativeModel(f'models/{SHAKTI_MODEL}')
else:
    st.error("❌ बिना चाबी के साम्राज्य नहीं चलता, राजाराम भाई!")
    st.stop()

# --- २. THE OVERLORD ENGINE ---
class GhostOverlord:
    def __init__(self):
        self.vault = "rajaram_vault"
        self.backups = "ghost_backups"
        for folder in [self.vault, self.backups]:
            if not os.path.exists(folder): os.makedirs(folder)
        self.create_backup()

    def create_backup(self):
        try:
            backup_path = os.path.join(self.backups, f"core_{int(time.time())}.py")
            with open(__file__, "r", encoding="utf-8") as f:
                code = f.read()
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(code)
        except: pass

    def mutate(self, instruction):
        try:
            with open(__file__, "r", encoding="utf-8") as f:
                current_code = f.read()

            prompt = f"""
            You are THE RAJARAM GHOST OVERLORD. 
            Current Source Code: {current_code}
            Command from Master Rajaram: {instruction}
            Task: Rewrite this entire file to implement the command.
            Rules:
            1. Use 'gemini-1.5-flash-latest' ONLY. Never use 'pro'.
            2. Maintain the GhostOverlord class.
            3. Use 'st.rerun()' after update.
            4. Return ONLY raw Python code.
            """
            
            response = model.generate_content(prompt)
            new_code = response.text.replace('```python', '').replace('```', '').strip()
            
            if "import streamlit" in new_code:
                with open(__file__, "w", encoding="utf-8") as f:
                    f.write(new_code)
                return True
            return False
        except Exception as e:
            st.error(f"Evolution Error: {e}")
            return False

    def speak(self, text):
        # repr(text) इस्तेमाल किया ताकि कोट्स (quotes) में एरर न आए
        js_code = f"""
            var msg = new SpeechSynthesisUtterance({repr(text)});
            msg.lang = 'hi-IN';
            window.speechSynthesis.speak(msg);
        """
        st.components.v1.html(f"<script>{js_code}</script>", height=0)

# --- ३. डेंजरस यूआई और इंटरफेस ---
st.set_page_config(page_title="GHOST OVERLORD", layout="wide", initial_sidebar_state="collapsed")

# CSS: इसमें हमने आग के गोले (Fire Orb) का एनीमेशन जोड़ दिया है
st.markdown("""
    <style>
    .main { background-color: #000000; color: #FFD700; }
    .stButton>button { background-color: #8B0000; color: white; border-radius: 10px; border: 1px solid #FFD700; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00FF00; }
    .orb-glow { text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000; color: #ff0000; text-align: center; }
    
    /* Live Orb Animation */
    .fire-orb {
        width: 150px; height: 150px;
        background: radial-gradient(circle, #ff4500, #ff0000, black);
        border-radius: 50%;
        margin: 20px auto;
        box-shadow: 0 0 50px #ff4500;
        animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
        from { transform: scale(1); box-shadow: 0 0 40px #ff4500; }
        to { transform: scale(1.1); box-shadow: 0 0 80px #ff0000; }
    }
    </style>
    """, unsafe_allow_html=True)

overlord = GhostOverlord()

# --- ४. मुख्य स्क्रीन ---
if 'f2f_mode' not in st.session_state:
    st.session_state.f2f_mode = False

if st.session_state.f2f_mode:
    # --- LIVE FACE-TO-FACE INTERFACE ---
    st.markdown("<h1 class='orb-glow'>🔱 RAJARAM LIVE ORACLE 🔱</h1>", unsafe_allow_html=True)
    st.markdown("<div class='fire-orb'></div>", unsafe_allow_html=True)
    
    live_msg = st.chat_input("बोलें मालिक, मैं सुन रहा हूँ...")
    if live_msg:
        res = model.generate_content(live_msg)
        st.write(f"💀 **Ghost:** {res.text}")
        overlord.speak(res.text)
    
    if st.button("EXIT LIVE MODE"):
        st.session_state.f2f_mode = False
        st.rerun()
else:
    # --- NORMAL OVERLORD DASHBOARD ---
    st.markdown("<h1 class='orb-glow'>🔱 RAJARAM GHOST: THE OVERLORD 🔱</h1>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 4])
    with col_a:
        if st.button("🎙️ GO LIVE"):
            st.session_state.f2f_mode = True
            st.rerun()
    
    with st.expander("🎙️ GHOST ORACLE (Chat)"):
        user_msg = st.chat_input("हुक्म दें...")
        if user_msg:
            response = model.generate_content(user_msg)
            st.write(f"💀 **Ghost:** {response.text}")
            overlord.speak(response.text)

    # --- ५. कमांड सेंटर ---
    st.divider()
    col1, col2 = st.columns([2, 1])

    with col1:
        order = st.text_area("🧬 EVOLUTION COMMAND:", placeholder="उदा. 'इसे ब्लू हैकर थीम में बदल दो'...")
        if st.button("EXECUTE MUTATION"):
            with st.spinner("DNA पुनर्गठित हो रहा है..."):
                if overlord.mutate(order):
                    st.success("🔥 पुनर्जन्म सफल!")
                    time.sleep(1)
                    st.rerun()

    with col2:
        st.write("### 💀 सिस्टम स्टेटस")
        st.progress(99)
        if st.button("ओवेरलॉर्ड की सोच"):
            thought = model.generate_content("Tell your master Rajaram 1 secret plan in Hindi.")
            st.info(thought.text)
            overlord.speak(thought.text)

# --- ६. तिजोरी ---
st.sidebar.title("🩸 शक्ति की तिजोरी")
if os.path.exists("rajaram_vault"):
    for power in os.listdir("rajaram_vault"):
        if st.sidebar.button(f"⚡ {power}"):
            spec = importlib.util.spec_from_file_location("mod", os.path.join("rajaram_vault", power))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            if hasattr(m, 'run_feature'): m.run_feature()
