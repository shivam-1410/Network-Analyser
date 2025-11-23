# Optional tiny wrapper for SQLite persistence (not used by default)
import sqlite3, os, json

DB = 'data/summary.sqlite3'
def save_summary(summary):
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS summaries (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')
    c.execute('INSERT INTO summaries (content) VALUES (?)', (json.dumps(summary),))
    conn.commit()
    conn.close()
