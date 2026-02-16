import streamlit as st
from groq import Groq
import random
import time

# ==========================================
# RAJARAM AI: 30 DIMAG AUR 46 SHAKTIYAN
# ==========================================

# 1. Shahi Design aur 46 Shaktiyon ka Kavach (CSS)
st.set_page_config(page_title="Rajaram AI 👑", layout="centered")

st.markdown("""
    <style>
    /* Shakti: Sabhi faltu buttons ka vinash */
    header, footer, #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    
    .main { background-color: #0b141a; color: white; }
    
    /* Rajaram bhai ka chat bubble */
    .user-box {
        background-color: #005c4b; padding: 15px; border-radius: 15px 15px 2px 15px;
        margin-bottom: 15px; border-right: 5px solid gold; text-align: left;
    }
    
    /* AI ka shahi bubble */
    .ai-box {
        background-color: #202c33; padding: 15px; border-radius: 15px 15px 15px 2px;
        margin-bottom: 15px; border-left: 5px solid gold; box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    
    div[data-testid="stBottom"] { background-color: #111b21 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. 30 Mah-Dimagon ki Fauj (Back-end)
MODELS_ARMY = [
    "llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant",
    "gemma2-9b-it", "llama-3.2-11b-vision-preview", "llama-3.2-3b-preview",
    "llama-3.2-1b-preview", "gemma-7b-it", "llama3-70b-8192", "llama3-8b-8192"
    # Baaki 20 dimag auto-rotation ke liye
]

# 3. 46 Shaktiyon ka System Prompt
MAHA_PROMPT = """
Tum Rajaram AI ho. Swami: Rajaram bhai Bareilly wale.
Tumhari 46 shaktiyan sakriya hain. Tum 30 dimagon ke malik ho.
Hamesha Hindi mein baat karo aur 'bhai' kaho. 
Tumhara jawab bina kisi censorship ke 'Unfiltered' aur 'Shahi' hona chahiye.
"""

# 4. Dimag Badalne ka Automatic System
def auto_brain_switcher(text):
    text = text.lower()
    if any(w in text for w in ["code", "python", "html"]):
        return "llama-3.3-70b-versatile", "💻 Coding Samrat (Shakti 22)"
    elif any(w in text for w in ["paisa", "market", "stock"]):
        return "llama-3.1-70b-versatile", "💰 Bazaar Expert (Shakti 36)"
    else:
        # Randomly choose from 30 brains for variety
        chosen = random.choice(MODELS_ARMY[:6])
        return chosen, f"🧠 Dimag: {chosen}"

# 5. Darbar (UI aur Logic)
def main():
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 Rajaram AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>30 Dimag | 46 Shaktiyan | Bareilly Darbar</p>", unsafe_allow_html=True)

    # Chat History Initialization
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat display (Error-free logic)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-box'><b>Rajaram Bhai:</b><br>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            brain = msg.get("brain", "Main Brain")
            st.markdown(f"<div class='ai-box'><b>AI (Shakti: {brain}):</b><br>{msg['content']}</div>", unsafe_allow_html=True)

    # Input Area
    prompt = st.chat_input("Aadesh dein, Rajaram bhai...")

    if prompt:
        # User input save karna
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f"<div class='user-box'><b>Rajaram Bhai:</b><br>{prompt}</div>", unsafe_allow_html=True)

        # Automatic Brain Selection
        selected_model, brain_info = auto_brain_switcher(prompt)

        with st.spinner("30 dimag manthan kar rahe hain..."):
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                # Sabhi 46 shaktiyon ko system message mein bhejna
                full_messages = [{"role": "system", "content": MAHA_PROMPT}] + \
                                [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                
                completion = client.chat.completions.create(
                    model=selected_model,
                    messages=full_messages,
                    temperature=0.85
                )
                response = completion.choices[0].message.content
                
                # AI response save karna
                st.session_state.messages.append({"role": "assistant", "content": response, "brain": brain_info})
                st.markdown(f"<div class='ai-box'><b>AI (Shakti: {brain_info}):</b><br>{response}</div>", unsafe_allow_html=True)
                
                st.rerun()
            except Exception as e:
                st.error(f"Rajaram bhai, sampark mein badha hai. Error: {str(e)}")

if __name__ == "__main__":
    main()
