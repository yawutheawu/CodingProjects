import feedparser

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
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published Date: {entry.published}") # Example of another attribute
        print("Attributes:")
        for key, value in entry.items():
            print(f"\t{key}: {value}")
        print("-" * 20)
else:
    print("Failed to parse RSS feed.")
    print(f"Error type: {type(feed.bozo_exception)}")
    print(f"Error message: {feed.bozo_exception}")