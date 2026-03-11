import os
import datetime

def inject_new_shakti(command, clean_code):
    """🔱 RAJARAM ADVANCED GHOST VAULT: SELF-CORRECTING & STYLED CODE"""
    try:
        # १. फाइल का नाम साफ़ सुथरा बनाना
        clean_name = "".join(x for x in command.lower().replace(" ", "_") if x.isalnum() or x == "_")[:15].strip("_")
        file_name = f"feature_{clean_name}.py"
        
        # २. ऑटो-इंडेंटेशन लॉजिक (Indentation Error का अंत)
        formatted_code = ""
        for line in clean_code.split("\n"):
            if line.strip():
                formatted_code += "    " + line + "\n"
            else:
                formatted_code += "\n"

        # ३. फाइल को राइट करना
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"# 🔱 GHOST POWER: {command}\n")
            f.write("import streamlit as st\n")
            f.write("from streamlit_mic_recorder import mic_recorder\n\n")
            f.write("def run_feature():\n")
            # बटन को गोल और छोटा (Icon जैसा) बनाने के लिए CSS
            f.write("    st.markdown('<style>div.stButton > button {padding:0; margin:0; width:40px !important; height:40px !important; border-radius:50% !important; border: 2px solid #FFD700 !important;}</style>', unsafe_allow_html=True)\n")
            f.write(formatted_code)
        
        return True
    except Exception as e:
        print(f"Vault Injection Error: {e}")
        return False
