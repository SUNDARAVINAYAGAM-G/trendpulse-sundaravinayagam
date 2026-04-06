TrendPulse — What's Actually Trending Right Now

Author: Sundaravinayagam
Project Type: End-to-End Data Pipeline
Language: Python
Tools: Requests, Pandas, NumPy, Matplotlib
Repository: trendpulse-sundaravinayagam

Project Overview

TrendPulse is a complete data pipeline project that collects trending stories from the HackerNews public API, cleans and processes the data, performs statistical analysis, and visualizes insights using charts.

This project demonstrates real-world data engineering and analytics workflow skills including:

    API Data Collection
    Data Cleaning and Processing
    Statistical Analysis
    Data Visualization
    File Handling (JSON and CSV)
    Error Handling
    Automated Data Pipeline

Project Pipeline

Task 1 → Task 2 → Task 3 → Task 4

Fetch JSON → Clean CSV → Analyze Data → Visualize Insights

Each task depends on the output of the previous task, forming a complete working data pipeline.

Project Structure

trendpulse-sundaravinayagam/

│

├── data/

│ ├── trends_YYYYMMDD.json

│ ├── trends_clean.csv

│ └── trends_analysed.csv

│

├── outputs/

│ ├── chart1_top_stories.png

│ ├── chart2_categories.png

│ ├── chart3_scatter.png

│ └── dashboard.png

│

├── task1_data_collection.py

├── task2_data_processing.py

├── task3_analysis.py

├── task4_visualization.py

│

└── README.md

Technologies Used

    Python
    Requests
    Pandas
    NumPy
    Matplotlib
    JSON
    CSV
    OS Module
    Datetime Module

Task 1 — Fetch Data from API

File:

task1_data_collection.py

Description:

This script connects to the HackerNews API and collects trending stories.

Features:

    Fetches top 500 story IDs
    Retrieves story details using API
    Categorizes stories using keyword matching
    Handles API request failures safely
    Waits 2 seconds between category loops
    Collects up to 25 stories per category
    Saves collected data into a JSON file

Output:

data/trends_YYYYMMDD.json

Example Console Output:

Collected 122 stories.

Saved to data/trends_20240115.json

Task 2 — Data Cleaning & Processing

File:

task2_data_processing.py

Description:

This script loads the JSON file created in Task 1, cleans the data using Pandas, and saves a cleaned dataset.

Cleaning Steps:

    Load JSON into Pandas DataFrame
    Remove duplicate stories using post_id
    Drop rows with missing values
    Convert score and num_comments to integers
    Remove low-quality stories (score < 5)
    Remove extra whitespace from titles
    Print row counts after each cleaning step

Output:

data/trends_clean.csv

Example Console Output:

Loaded 122 stories

After removing duplicates: 120

After removing nulls: 118

After removing low scores: 114

Saved 114 rows to data/trends_clean.csv

Stories per category:

technology 22

worldnews 24

sports 21

science 24

entertainment 23

Task 3 — Data Analysis with Pandas & NumPy

File:

task3_analysis.py

Description:

This script analyzes the cleaned dataset using Pandas and NumPy to compute statistics and generate new columns.

Analysis Performed:

    Display first 5 rows
    Show dataset shape
    Calculate average score
    Calculate average comments
    Compute mean, median, and standard deviation using NumPy
    Find highest and lowest scores
    Identify category with most stories
    Identify story with most comments

New Columns Added:

engagement

num_comments / (score + 1)

is_popular

True if score > average score

False otherwise

Output:

data/trends_analysed.csv

Example Console Output:

Loaded data: (114, 7)

Average score: 12450

Average comments: 342

Mean score: 12450

Median score: 8200

Std deviation: 9870

Max score: 87432

Min score: 5

Most stories in: technology

Most commented story:

AI model beats humans at coding — 4891 comments

Saved to data/trends_analysed.csv

Task 4 — Data Visualization

File:

task4_visualization.py

Description:

This script creates visual charts from the analyzed dataset using Matplotlib and saves them as PNG files.

Charts Created:

Chart 1 — Top 10 Stories by Score

    Horizontal bar chart
    Shows highest scoring stories
    Titles shortened to 50 characters

Saved as:

outputs/chart1_top_stories.png

Chart 2 — Stories per Category

    Bar chart
    Displays number of stories in each category
    Different color for each category

Saved as:

outputs/chart2_categories.png

Chart 3 — Score vs Comments

    Scatter plot
    X-axis: Score
    Y-axis: Number of comments
    Different colors for popular vs non-popular stories

Saved as:

outputs/chart3_scatter.png

Bonus — Dashboard

All charts combined into a single figure.

Saved as:

outputs/dashboard.png

Installation

Install required libraries:

pip install requests pandas numpy matplotlib

How to Run the Project

Run the pipeline step-by-step.

Step 1 — Collect Data

python task1_data_collection.py

Step 2 — Clean Data

python task2_data_processing.py

Step 3 — Analyze Data

python task3_analysis.py

Step 4 — Visualize Data

python task4_visualization.py

Expected Output Files

data/

trends_YYYYMMDD.json

trends_clean.csv

trends_analysed.csv

outputs/

chart1_top_stories.png

chart2_categories.png

chart3_scatter.png

dashboard.png

Key Features

    End-to-end data pipeline
    Real-time API data collection
    Data cleaning and validation
    Statistical analysis using NumPy
    Data visualization using Matplotlib
    Automated file generation
    Error handling
    Modular Python scripts

Submission Checklist

✔ All scripts run without errors
✔ JSON file created
✔ CSV file created
✔ Analysis file created
✔ Charts saved as PNG
✔ Dashboard generated
✔ Code properly commented
✔ README file included

Future Improvements

    Add logging system
    Export charts automatically
    Build interactive dashboard using Streamlit
    Schedule automated data collection
    Add real-time analytics

Author

Sundaravinayagam

Data Analyst

Python Developer

TrendPulse — Data Pipeline Project
