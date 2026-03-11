import os
import datetime

def inject_new_shakti(command, clean_code):
    """🔱 यह फंक्शन हर आदेश के लिए एक अलग 'feature_xxx.py' फाइल बनाएगा"""
    try:
        # फाइल का नाम आदेश के अनुसार छोटा और साफ (e.g., feature_voice_mode.py)
        clean_name = command.lower().replace(" ", "_")[:15]
        file_name = f"feature_{clean_name}.py"
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # नई फाइल लिखना
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"# 🔱 GHOST POWER: {command}\n")
            f.write(f"# Created: {timestamp}\n\n")
            f.write("import streamlit as st\n")
            f.write("from streamlit_mic_recorder import mic_recorder\n\n")
            f.write("def run_feature():\n")
            # कोड को थोडा अंदर (Indent) धकेलना ताकि 'def' के नीचे आए
            indented_code = "\n".join(["    " + line for line in clean_code.split("\n")])
            f.write(indented_code)
        
        return True
    except Exception as e:
        print(f"Vault Injection Error: {e}")
        return False
