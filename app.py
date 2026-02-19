import streamlit as st
from groq import Groq
import random

# --- 1. 30 दिमागों की मास्टर लिस्ट और उनके अलग-अलग काम ---
BRAIN_SYSTEM = {
    "Brain-1": "Security Analysis", "Brain-2": "Creative Coding", "Brain-3": "Future Prediction",
    "Brain-4": "Data Mining", "Brain-5": "Satellite Tracking", "Brain-6": "Financial Strategy",
    "Brain-7": "Logic Solving", "Brain-8": "Image Generation", "Brain-9": "Voice Synthesis",
    "Brain-10": "System Hacking", "Brain-11": "Global Networking", "Brain-12": "Memory Storage",
    "Brain-13": "Neural Mapping", "Brain-14": "Bio-Scanning", "Brain-15": "Speed Optimization",
    "Brain-16": "Encryption Expert", "Brain-17": "History Analysis", "Brain-18": "Legal Research",
    "Brain-19": "Weather Control", "Brain-20": "Robotics Control", "Brain-21": "AI Training",
    "Brain-22": "Physics Engine", "Brain-23": "Mathematical Master", "Brain-24": "Language Translator",
    "Brain-25": "Crisis Manager", "Brain-26": "Health Diagnostics", "Brain-27": "Music Creation",
    "Brain-28": "Space Exploration", "Brain-29": "Traffic Control", "Brain-30": "Final Admin Soul"
}

# --- 2. कनेक्शन (Secrets से) ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- 3. दिमाग बदलने का सिस्टम (Logic) ---
def get_best_brain(user_input):
    # यह सिस्टम सवाल देखकर सही दिमाग चुनता है
    if "photo" in user_input.lower(): return "Brain-8"
    if "code" in user_input.lower(): return "Brain-2"
    if "security" in user_input.lower(): return "Brain-1"
    # अगर कुछ समझ न आए तो रैंडम दिमाग चुनना
    return random.choice(list(BRAIN_SYSTEM.keys()))

# --- 4. मुख्य इंटरफेस ---
st.title("RAJARAM-X: 30 BRAINS")

user_query = st.chat_input("अपना आदेश यहाँ लिखें...")

if user_query:
    # दिमाग बदलना
    active_brain = get_best_brain(user_query)
    brain_task = BRAIN_SYSTEM[active_brain]
    
    st.write(f"🧠 **सक्रिय दिमाग:** {active_brain} | **कार्य:** {brain_task}")
    
    # Groq Model से जवाब लेना
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"तुम Rajaram-X के {active_brain} हो। तुम्हारा काम {brain_task} है।"},
                {"role": "user", "content": user_query}
            ]
        )
        st.success(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")

# --- 5. साइडबार में सभी 30 दिमागों की लिस्ट ---
with st.sidebar:
    st.header("Brain Cluster Status")
    for b_id, task in BRAIN_SYSTEM.items():
        st.write(f"🟢 {b_id}: {task}")
