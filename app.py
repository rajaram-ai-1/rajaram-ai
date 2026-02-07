import streamlit as st
import google.generativeai as genai

# आपकी 6 चाबियाँ (Keys)
all_keys = ["KEY_1", "KEY_2", "KEY_3", "KEY_4", "KEY_5", "KEY_6"]

# गूगल के अलग-अलग 'दिमाग' (Models)
all_models = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-1.0-pro']

def get_super_response(user_input):
    # यह लूप हर चाबी को चेक करेगा
    for key in all_keys:
        genai.configure(api_key=key)
        
        # यह लूप हर चाबी के अंदर अलग-अलग 'दिमाग' को चेक करेगा
        for model_name in all_models:
            try:
                model = genai.GenerativeModel(model_name)
                # आपकी डायरी वाले निर्देश
                full_prompt = f"System: You are Rajaram AI. Friendly and motivational brother. Serious about studies. User: {user_input}"
                response = model.generate_content(full_prompt)
                
                # अगर यहाँ जवाब मिल गया, तो लौट जाओ!
                return response.text
                
            except Exception:
                # अगर यह मॉडल या चाबी काम नहीं कर रही, तो अगले पर जाओ
                continue
                
    return "मालिक, आज गूगल के सारे दिमाग थक गए हैं। कृपया थोड़ी देर बाद आएं।"
