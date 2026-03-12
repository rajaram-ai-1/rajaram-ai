import streamlit as st
import os
import sys
import subprocess
import google.generativeai as genai

# --- ईश्वरीय शक्ति: Secrets से चाबी उठाना ---
# यहाँ हम 'GEMINI_KEY' और 'gemini_key' दोनों चेक करेंगे
api_key = st.secrets.get("GEMINI_KEY") or st.secrets.get("gemini_key")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro')
        # st.success("🔱 चाबी मिल गई, महा-शक्ति तैयार है!") # टेस्टिंग के लिए इसे हटा सकते हैं
    except Exception as e:
        st.error(f"⚠️ चाबी तो मिली पर काम नहीं कर रही: {e}")
else:
    st.error("⚠️ Maalik, Streamlit Settings में 'GEMINI_KEY' अभी भी नहीं दिख रही!")

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
