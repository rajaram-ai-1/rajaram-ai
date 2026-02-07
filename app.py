import streamlit as st
import requests

# --- 1. अपनी नई API चाबी यहाँ डालें ---
GOOGLE_API_KEY = "AIzaSyAe6Y5uWuWCXkT1OlAZpy47Y2ytmgxo0Vg"

def get_final_victory(user_input):
    # यह URL सबसे लेटेस्ट और सबसे पावरफुल है
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": user_input}]}]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        
        # अगर गूगल ने ब्लॉक किया है तो यहाँ पता चलेगा
        if response.status_code != 200:
            return f"गूगल ने गेट बंद कर दिया है! वजह: {data.get('error', {}).get('message', 'Unknown')}"
            
        if 'candidates' in result:
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "गूगल के पास जवाब नहीं है, पर रास्ता खुला है।"
    except Exception as e:
        return f"रास्ते में रुकावट: {str(e)}"

# --- UI ---
st.title("👑 Rajaram AI (R-Paar)")

query = st.text_input("क्या बोलना है गूगल को?")
if st.button("हमला करें ⚔️"):
    if query:
        result = get_final_victory(query)
        st.write(result)
