import sqlite3
from datetime import datetime

# --- 🔱 DATABASE ARCHITECT (तिजोरी बनाना) ---
def create_brain_vault():
    conn = sqlite3.connect("rajaram_ai_memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS brain_vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            user_say TEXT,
            ai_reply TEXT,
            mood TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()

# --- 🔱 SAVING LOGIC (याददाश्त में लिखना) ---
def save_to_memory(user_id, message, response, current_mood="Neutral"):
    conn = sqlite3.connect("rajaram_ai_memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO brain_vault (user_id, user_say, ai_reply, mood, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, message, response, current_mood, datetime.now()))
    conn.commit()
    conn.close()

# --- 🔱 RECALL LOGIC (पुरानी बातें याद करना) ---
def get_past_context(user_id, limit=5):
    conn = sqlite3.connect("rajaram_ai_memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_say, ai_reply FROM brain_vault 
        WHERE user_id = ? 
        ORDER BY timestamp DESC LIMIT ?
    """, (user_id, limit))
    history = cursor.fetchall()
    conn.close()
    return history

# फाइल रन होते ही डेटाबेस तैयार हो जाए
create_brain_vault()
