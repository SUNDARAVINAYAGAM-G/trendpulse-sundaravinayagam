"""
Task 4 — Visualizations
TrendPulse: What's Actually Trending Right Now

This script loads analysed data from Task 3 and creates
three charts using Matplotlib, then combines them into
a single dashboard.

Charts:
1. Top 10 stories by score (horizontal bar chart)
2. Stories per category (bar chart)
3. Score vs Comments (scatter plot)

All charts are saved as PNG files in the outputs/ folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------
# Step 1 — Setup
# ---------------------------------------

file_path = "data/trends_analysed.csv"

# Check if file exists
if not os.path.exists(file_path):
    print("File not found:", file_path)
    exit()

# Load data
df = pd.read_csv(file_path)

# Create outputs folder if it doesn't exist
output_folder = "outputs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ---------------------------------------
# Helper function — shorten long titles
# ---------------------------------------

def shorten_title(title):
    if len(title) > 50:
        return title[:50] + "..."
    return title

# ---------------------------------------
# Chart 1 — Top 10 Stories by Score
# ---------------------------------------

top10 = df.nlargest(10, "score").copy()

top10["short_title"] = top10["title"].apply(shorten_title)

plt.figure()

plt.barh(
    top10["short_title"],
    top10["score"]
)

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("outputs/chart1_top_stories.png")

plt.close()

# ---------------------------------------
# Chart 2 — Stories per Category
# ---------------------------------------

category_counts = df["subreddit"].value_counts()

plt.figure()

plt.bar(
    category_counts.index,
    category_counts.values,
    color=["red", "blue", "green", "orange", "purple"]
)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.tight_layout()

plt.savefig("outputs/chart2_categories.png")

plt.close()

# ---------------------------------------
# Chart 3 — Score vs Comments
# ---------------------------------------

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()

plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

plt.legend()

plt.tight_layout()

plt.savefig("outputs/chart3_scatter.png")

plt.close()

# ---------------------------------------
# Bonus — Combined Dashboard
# ---------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1 in dashboard
axes[0].barh(
    top10["short_title"],
    top10["score"]
)

axes[0].set_title("Top 10 Stories")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Title")

axes[0].invert_yaxis()

# Chart 2 in dashboard
axes[1].bar(
    category_counts.index,
    category_counts.values
)

axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

# Chart 3 in dashboard
axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

axes[2].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")

axes[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.tight_layout()

plt.savefig("outputs/dashboard.png")

plt.close()

# ---------------------------------------
# Final confirmation
# ---------------------------------------

print("Charts saved successfully in outputs/ folder.")