import feedparser
from datetime import datetime

trackedUsers = ["djkarate1","yawutheawu"]

rss_url = 'https://letterboxd.com/yawutheawu/rss/'


feed = feedparser.parse(rss_url)

# Check if the feed was parsed successfully
# Note: feed.status might not be present in all versions, checking bozo is a safer approach for errors

print(f"Bozo status: {feed.bozo}") # 0/False means no parsing errors, 1/True mean error
print(f"HTTP status: {feed.status}") # HTTP status code

if feed.bozo == 0:
    print(f"Feed Title: {feed.feed.title}")
    print(f"Number of entries: {len(feed.entries)}\n")

    # Iterate through each entry (article/post) in the feed
    for entry in feed.entries:
        print(f"Film: {entry.letterboxd_filmtitle} ({entry.letterboxd_filmyear})")
        print(f"Watched on {datetime.strptime(entry.letterboxd_watcheddate,"%Y-%M-%d").strftime("%b %d, %Y")}")
        print(f"Review Link: {entry.link}")
        print(f"Published Date: {entry.published}") # Example of another attribute
        print(f"Rating: {entry.letterboxd_memberrating}/5.0")
        print(f"Liked?: {entry.letterboxd_memberlike}")
        print(f"First Watch?: {(lambda x: "No" if x == "Yes" else "Yes")(entry.letterboxd_rewatch)}")
        print("-" * 20)
else:
    print("Failed to parse RSS feed.")
    print(f"Error type: {type(feed.bozo_exception)}")
    print(f"Error message: {feed.bozo_exception}")