"""
Netflix Data Analysis with Pandas
--------------------------------
A beginner-friendly project that shows basic Pandas operations
and simple Matplotlib charts.
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1) LOAD DATA
# -----------------------------
# We load the CSV file into a Pandas DataFrame using pd.read_csv().
# A DataFrame is like a table (rows and columns).
# Make sure your CSV file is named 'netflix_titles.csv' and placed
# in the same folder as this script.
df = pd.read_csv("netflix_titles.csv")

# -----------------------------
# 2) QUICK LOOK AT THE DATA
# -----------------------------
# shape tells us how many rows and columns are in the dataset.
print("Dataset shape (rows, columns):", df.shape)
print("\n")

# head() shows the first 5 rows by default.
# This helps us quickly preview what the data looks like.
print("First 5 rows:")
print(df.head())
print("\n")

# info() shows column names, data types, and non-null counts.
# Very useful for understanding structure and spotting missing data.
print("Dataset info:")
print(df.info())
print("\n")

# -----------------------------
# 3) MISSING VALUES ANALYSIS
# -----------------------------
# isnull() returns True/False for each cell if value is missing.
# sum() then counts how many missing values each column has.
print("Missing values in each column:")
print(df.isnull().sum())
print("\n")

# -----------------------------
# 4) SIMPLE DATA CLEANING
# -----------------------------
# dropna() removes rows with missing values.
# Here, we create a cleaned copy so original df stays unchanged.
df_clean = df.dropna(subset=["country", "listed_in", "release_year"])

print("Shape before cleaning:", df.shape)
print("Shape after dropna on country/listed_in/release_year:", df_clean.shape)
print("\n")

# -----------------------------
# 5) UNIQUE VALUES
# -----------------------------
# unique() gives unique values from a column.
# We use it for the type column (usually Movie or TV Show).
print("Unique content types:")
print(df["type"].unique())
print("\n")

# -----------------------------
# 6) VALUE COUNTS
# -----------------------------
# value_counts() counts frequency of each category.
# Great for quick summaries.
print("Count of each content type:")
print(df["type"].value_counts())
print("\n")

# -----------------------------
# 7) FILTERING EXAMPLES
# -----------------------------
# Filtering movies only.
movies_df = df[df["type"] == "Movie"]
print("Number of movies:", movies_df.shape[0])

# Filtering titles released in or after 2020.
recent_titles_df = df[df["release_year"] >= 2020]
print("Number of titles released in or after 2020:", recent_titles_df.shape[0])
print("\n")

# -----------------------------
# 8) SORTING EXAMPLE
# -----------------------------
# sort_values() sorts the DataFrame by a column.
# ascending=False means newest release years first.
sorted_by_year = df.sort_values(by="release_year", ascending=False)
print("Top 10 newest titles by release year:")
print(sorted_by_year[["title", "release_year"]].head(10))
print("\n")

# -----------------------------
# 9) GENRE ANALYSIS
# -----------------------------
# The listed_in column may contain multiple genres separated by commas.
# str.split(', ') breaks them into lists.
# explode() turns each genre into its own row.
# Then value_counts() gives top genres.
genre_counts = (
    df_clean["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
)

print("Top 10 genres:")
print(genre_counts.head(10))
print("\n")

# -----------------------------
# 10) COUNTRY ANALYSIS
# -----------------------------
# country can also have multiple countries separated by commas.
# We split and explode the same way.
country_counts = (
    df_clean["country"]
    .str.split(", ")
    .explode()
    .value_counts()
)

print("Top 10 countries:")
print(country_counts.head(10))
print("\n")

# -----------------------------
# 11) SIMPLE VISUALIZATIONS
# -----------------------------
# Chart 1: Bar chart of content type counts.
plt.figure(figsize=(6, 4))
df["type"].value_counts().plot(kind="bar", color=["#1f77b4", "#ff7f0e"])
plt.title("Number of Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 2: Top 10 genres bar chart.
plt.figure(figsize=(10, 5))
genre_counts.head(10).plot(kind="bar", color="#2ca02c")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Chart 3: Top 10 countries bar chart.
plt.figure(figsize=(10, 5))
country_counts.head(10).plot(kind="bar", color="#d62728")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
