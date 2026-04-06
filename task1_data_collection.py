"""
Task 1 — Fetch Data from API
TrendPulse: What's Actually Trending Right Now
"""
import requests
import json
import os
import time
from datetime import datetime

# -----------------------------
# API URLs
# -----------------------------

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Required header
headers = {
    "User-Agent": "TrendPulse/1.0"
}

# -----------------------------
# Categories and Keywords
# -----------------------------

categories = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "nfl", "nba", "fifa", "sport", "game",
        "team", "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "netflix",
        "game", "book", "show", "award", "streaming"
    ]
}

# -----------------------------
# Step 1 — Fetch top story IDs
# -----------------------------

try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    response.raise_for_status()

    story_ids = response.json()

    # Take only first 500
    story_ids = story_ids[:500]

except requests.exceptions.RequestException as e:
    print("Error fetching top stories:", e)
    story_ids = []

# -----------------------------
# Storage for collected posts
# -----------------------------

posts = []

# Track how many posts per category
category_counts = {
    category: 0 for category in categories
}

# -----------------------------
# Step 2 — Fetch story details
# -----------------------------

for category, keywords in categories.items():

    print(f"Processing category: {category}")

    for story_id in story_ids:

        # Stop if category already has 25 posts
        if category_counts[category] >= 25:
            break

        try:
            url = ITEM_URL.format(story_id)

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            story = response.json()

            # Skip if story is None
            if not story:
                continue

            title = story.get("title", "")

            # Case-insensitive matching
            title_lower = title.lower()

            # Check keyword match
            if any(keyword in title_lower for keyword in keywords):

                post = {
                    "post_id": story.get("id"),
                    "title": title,
                    "subreddit": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }

                posts.append(post)

                category_counts[category] += 1

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch story {story_id}: {e}")
            continue

    # Required: sleep once per category
    time.sleep(2)

# -----------------------------
# Step 3 — Save JSON file
# -----------------------------

# Create data folder if it doesn't exist
data_folder = "data"

if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Generate filename
date_str = datetime.now().strftime("%Y%m%d")

filename = f"{data_folder}/trends_{date_str}.json"

# Save JSON
with open(filename, "w", encoding="utf-8") as file:
    json.dump(posts, file, indent=4)

# -----------------------------
# Final Output
# -----------------------------

print(
    f"Collected {len(posts)} posts. "
    f"Saved to {filename}"
)