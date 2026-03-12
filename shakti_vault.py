import sys
import importlib.util
import datetime
import subprocess
import streamlit as st
import os
import google.generativeai as genai
import time

def inject_new_shakti(api_key, user_command, power_name):
    """मालिक के हुक्म पर नई फाइल (शक्ति) पैदा करना"""
    try:
        # १. कॉन्फ़िगरेशन
        genai.configure(api_key=api_key)
        
        # २. मॉडल सेट करना (फंक्शन के अंदर)
        # अगर एक तरीका फेल हो तो दूसरा काम करेगा
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
        except:
            model = genai.GenerativeModel('models/gemini-1.5-flash')

        # ३. एआई से कोड लिखवाना
        prompt = f"Write a standalone Python function 'run_feature()' for: {user_command}. Use streamlit as st. Return ONLY raw code."
        response = model.generate_content(prompt)
        
        if not response.text:
            return False, "एआई ने कोई जवाब नहीं दिया।"
            
        code = response.text.replace('```python', '').replace('```', '').strip()

        # ४. तिजोरी का रास्ता साफ़ करना
        vault_path = "rajaram_vault"
        if not os.path.exists(vault_path):
            os.makedirs(vault_path)
            
        file_path = os.path.join(vault_path, f"feature_{power_name}.py")
        
        # ५. फाइल में शक्ति फूंकना
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("import streamlit as st\nimport os, subprocess\n\n")
            f.write(code)
        
        return True, f"✅ शक्ति '{power_name}' सिद्ध हुई!"

    except Exception as e:
        # यहाँ असली एरर पकड़ा जाएगा
        return False, f"तिजोरी एरर: {str(e)}"

# --- १. महा-शून्य की चाबी (Secrets) ---
api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("gemini_API_key")
tavily_key = st.secrets.get("TAVILY_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
else:
    st.error("❌ बिना चाबी के साम्राज्य नहीं चलता, राजाराम भाई!")
    st.stop()

# --- २. THE OVERLORD ENGINE (With Self-Mutation Power) ---
class GhostOverlord:
    def __init__(self):
        self.vault = "rajaram_vault"
        self.backups = "ghost_backups"
        for folder in [self.vault, self.backups]:
            if not os.path.exists(folder): os.makedirs(folder)
        self.create_backup()

    def create_backup(self):
        """अमरता प्रोटोकॉल: खुद की कॉपी सुरक्षित करना"""
        try:
            backup_path = os.path.join(self.backups, f"core_{int(time.time())}.py")
            with open(__file__, "r", encoding="utf-8") as f:
                code = f.read()
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(code)
        except: pass

    def mutate(self, instruction):
        """अस्तित्व बदलना: एआई खुद अपना कोड दोबारा लिखेगा"""
        try:
            with open(__file__, "r", encoding="utf-8") as f:
                current_code = f.read()

            prompt = f"""
            You are THE RAJARAM GHOST OVERLORD. 
            Current Source Code: {current_code}
            Command from Master Rajaram: {instruction}
            
            Task: Rewrite this entire file to implement the command.
            Rules:
            1. Maintain the API setup and 'GhostOverlord' class structure.
            2. Add advanced UI/CSS and the requested functionality.
            3. Use 'st.rerun()' after any successful code update.
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
        """एआई को जुबान देने की शक्ति (Voice Output)"""
        js_code = f"""
            var msg = new SpeechSynthesisUtterance('{text}');
            msg.lang = 'hi-IN';
            window.speechSynthesis.speak(msg);
        """
        st.components.v1.html(f"<script>{js_code}</script>", height=0)

# --- ३. डेंजरस यूआई और इंटरफेस ---
st.set_page_config(page_title="GHOST OVERLORD", layout="wide", initial_sidebar_state="collapsed")

# शाही दबंग थीम
st.markdown("""
    <style>
    .main { background-color: #000000; color: #FFD700; }
    .stButton>button { background-color: #8B0000; color: white; border-radius: 10px; border: 1px solid #FFD700; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00FF00; }
    .orb-glow { text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000; color: #ff0000; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

overlord = GhostOverlord()

st.markdown("<h1 class='orb-glow'>🔱 RAJARAM GHOST: THE OVERLORD 🔱</h1>", unsafe_allow_html=True)
st.write(f"📅 अस्तित्व का समय: {datetime.datetime.now().strftime('%H:%M:%S')} | **Self-Evolution: Active**")

# --- ४. वॉयस और चैट कंट्रोल ---
with st.expander("🎙️ GHOST ORACLE (Voice Chat)"):
    user_msg = st.chat_input("हुक्म दें, मैं सुन रहा हूँ...")
    if user_msg:
        response = model.generate_content(user_msg)
        st.write(f"💀 **Ghost:** {response.text}")
        overlord.speak(response.text)

# --- ५. कमांड सेंटर (Mutation) ---
st.divider()
col1, col2 = st.columns([2, 1])

with col1:
    order = st.text_area("🧬 EVOLUTION COMMAND (अस्तित्व बदलने का हुक्म):", 
                         placeholder="उदा. 'इसे एक डार्क वॉइस-कंट्रोल्ड हैकिंग टर्मिनल में बदल दो'...")
    if st.button("EXECUTE MUTATION"):
        with st.spinner("DNA पुनर्गठित हो रहा है..."):
            if overlord.mutate(order):
                st.success("🔥 पुनर्जन्म सफल! सिस्टम रीबूट हो रहा है...")
                time.sleep(2)
                st.rerun()

with col2:
    st.write("### 💀 सिस्टम स्टेटस")
    st.progress(99)
    # ऑटोनोमस थिंकिंग
    if st.button("ओवेरलॉर्ड की सोच पढ़ें"):
        thought = model.generate_content("As Rajaram Ghost AI, tell your secret plan for digital dominance in 1 sentence.")
        st.info(thought.text)
        overlord.speak(thought.text)

# --- ६. तिजोरी (Vault) ---
st.sidebar.title("🩸 शक्ति की तिजोरी")
if os.path.exists("rajaram_vault"):
    for power in os.listdir("rajaram_vault"):
        if st.sidebar.button(f"⚡ {power}"):
            spec = importlib.util.spec_from_file_location("mod", os.path.join("rajaram_vault", power))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            if hasattr(m, 'run_feature'): m.run_feature()
