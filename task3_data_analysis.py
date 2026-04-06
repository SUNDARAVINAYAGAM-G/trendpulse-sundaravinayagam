"""
Task 3 — Analysis with Pandas & NumPy
TrendPulse: What's Actually Trending Right Now

This script loads the cleaned CSV from Task 2,
performs analysis using Pandas and NumPy,
adds new calculated columns, and saves the result.

Tasks completed:
- Load and explore dataset
- Compute statistics using NumPy
- Identify top category and most commented story
- Add engagement and is_popular columns
- Save analysed dataset to CSV
"""

import pandas as pd
import numpy as np
import os

# ---------------------------------------
# Step 1 — Load Data
# ---------------------------------------

file_path = "data/trends_clean.csv"

# Check file exists
if not os.path.exists(file_path):
    print("File not found:", file_path)
    exit()

df = pd.read_csv(file_path)

# Print shape
print("Loaded data:", df.shape)

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# ---------------------------------------
# Basic averages
# ---------------------------------------

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", int(avg_score))
print("Average comments:", int(avg_comments))

# ---------------------------------------
# Step 2 — NumPy Statistics
# ---------------------------------------

scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")

print("Mean score   :", int(mean_score))
print("Median score :", int(median_score))
print("Std deviation:", int(std_score))
print("Max score    :", int(max_score))
print("Min score    :", int(min_score))

# Category with most stories
category_counts = df["subreddit"].value_counts()

top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Most commented story
max_comments_index = df["num_comments"].idxmax()

top_story_title = df.loc[max_comments_index, "title"]
top_story_comments = df.loc[max_comments_index, "num_comments"]

print(
    f'\nMost commented story: "{top_story_title}" '
    f'— {top_story_comments} comments'
)

# ---------------------------------------
# Step 3 — Add New Columns
# ---------------------------------------

# engagement formula
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular flag
df["is_popular"] = df["score"] > avg_score

# ---------------------------------------
# Step 4 — Save Result
# ---------------------------------------

output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print("\nSaved to", output_file)