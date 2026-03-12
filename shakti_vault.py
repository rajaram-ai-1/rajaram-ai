import streamlit as st
import os
import sys
import subprocess
import google.generativeai as genai

# --- १. ईश्वरीय शक्ति: Secrets से चाबी उठाना ---
try:
    # यह लाइन सीधे Streamlit के Secrets से 'GEMINI_KEY' नाम की चाबी उठाएगी
    GEMINI_API_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error("⚠️ Maalik, Streamlit Settings में 'GEMINI_KEY' नहीं मिली!")

class MahaShaktiEngine:
    def __init__(self):
        self.vault_path = "rajaram_vault"
        if not os.path.exists(self.vault_path):
            os.makedirs(self.vault_path)
        
        self.safety_limits = {
            'forbidden': ['os.system("rm -rf', 'os.remove("/")']
        }

    def think_and_inject(self, user_command, power_name):
        """शक्ति का निर्माण और सुरक्षा जांच"""
        try:
            prompt = f"You are RAJARAM GHOST AI. Write a standalone Python function 'run_feature()' for: {user_command}. Return ONLY raw code."
            response = model.generate_content(prompt)
            code = response.text.replace('```python', '').replace('```', '').strip()

            # सुरक्षा जांच
            for danger in self.safety_limits['forbidden']:
                if danger in code:
                    return False, "🚫 सुरक्षा ब्लॉक: खतरनाक कोड!"

            # फाइल सेव करना
            file_path = os.path.join(self.vault_path, f"feature_{power_name}.py")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("import streamlit as st\nimport os, subprocess\n\n")
                f.write(code)
            
            return True, f"✅ शक्ति '{power_name}' सिद्ध हुई!"
        except Exception as e:
            return False, f"⚠️ ब्रह्मांडीय त्रुटि: {str(e)}"
