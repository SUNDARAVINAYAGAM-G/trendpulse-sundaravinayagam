import pandas as pd
import os


DATA_FOLDER = "data"


def get_latest_json():
    """Find latest JSON file in data folder"""
    files = [f for f in os.listdir(DATA_FOLDER) if f.startswith("trends_") and f.endswith(".json")]

    if not files:
        print("No JSON file found in data/ folder")
        return None

    files.sort(reverse=True)
    return os.path.join(DATA_FOLDER, files[0])


def main():
    file_path = get_latest_json()

    if not file_path:
        return

    # ---------------------------
    # 1. LOAD JSON
    # ---------------------------
    df = pd.read_json(file_path)
    print(f"Loaded {len(df)} stories from {file_path}\n")

    # ---------------------------
    # 2. CLEAN DATA
    # ---------------------------

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")

    # Remove missing values
    before = len(df)
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")

    # Fix data types
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

    # Remove rows that became NaN after conversion
    df = df.dropna(subset=["score", "num_comments"])

    # Convert to int
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Remove low quality (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Clean whitespace in title
    df["title"] = df["title"].str.strip()

    # ---------------------------
    # 3. SAVE CSV
    # ---------------------------

    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)

    print(f"\nSaved {len(df)} rows to {output_file}\n")

    # ---------------------------
    # SUMMARY
    # ---------------------------

    print("Stories per category:")
    print(df["subreddit"].value_counts())


if __name__ == "__main__":
    main()