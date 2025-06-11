import sqlite3
import requests

# Your YouTube Data API v3 key here
API_KEY = "AIzaSyD-mffGgF69fuhW_wzDcS_RL1Jzjjq7Mls"  # 🔁 Replace this with your actual API key
REGION_CODE = "IN"
MAX_RESULTS = 10

# Step 1: Connect to SQLite database
conn = sqlite3.connect('youtube_trending.db')
cursor = conn.cursor()

# Step 2: Create the table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trending_videos (
        id TEXT PRIMARY KEY,
        title TEXT,
        channel TEXT,
        views INTEGER
    )
''')

# Step 3: Fetch trending videos from YouTube API
url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={REGION_CODE}&maxResults={MAX_RESULTS}&key={API_KEY}"
response = requests.get(url)
data = response.json()

if 'items' not in data:
    print("❌ Error fetching data. Check API key or quota.")
else:
    for item in data['items']:
        video_id = item['id']
        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        views = int(item['statistics'].get('viewCount', 0))

        cursor.execute('''
            INSERT OR REPLACE INTO trending_videos (id, title, channel, views)
            VALUES (?, ?, ?, ?)
        ''', (video_id, title, channel, views))

    conn.commit()

    # ✅ Output Summary
    print("\n✅ Successfully fetched trending videos from YouTube API.")
    print(f"📥 Fetched {len(data['items'])} videos for region: {REGION_CODE}")
    print("💾 Stored videos in local database (youtube_trending.db)")

    # 🎥 Show all titles
    print("\n🎥 Trending Video Titles:\n")
    cursor.execute("SELECT title FROM trending_videos ORDER BY views DESC")
    rows = cursor.fetchall()

    for i, row in enumerate(rows, 1):
        print(f"{i}. {row[0]}")

# Step 4: Close the database
conn.close()
