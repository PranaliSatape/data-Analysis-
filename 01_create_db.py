import sqlite3

# Create or connect to DB
conn = sqlite3.connect('youtube_trending.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS trending_videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    channel TEXT,
    views INTEGER,
    category_id TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database created.")
