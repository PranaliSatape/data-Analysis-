import sqlite3

# Connect to the database
conn = sqlite3.connect('youtube_trending.db')
cursor = conn.cursor()

# Fetch the top 1 trending video
cursor.execute("SELECT title, channel, views FROM trending_videos ORDER BY views DESC LIMIT 1")
top_video = cursor.fetchone()

print(" Top Trending Video Right Now:\n")
print(f" Title   : {top_video[0]}")
print(f" Channel : {top_video[1]}")
print(f" Views   : {top_video[2]}")

# Fetch top 5 trending videos
cursor.execute("SELECT title, channel, views FROM trending_videos ORDER BY views DESC LIMIT 5")
top_videos = cursor.fetchall()

print("\n Quick Look: Top 5 Trending Videos\n")
for idx, video in enumerate(top_videos, start=1):
    title = (video[0][:50] + "...") if len(video[0]) > 50 else video[0]
    print(f"{idx}. {title} — {video[1]} ({video[2]} views)")

# Close the connection
conn.close()
