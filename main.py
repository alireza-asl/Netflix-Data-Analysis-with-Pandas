import pandas as pd
import matplotlib.pyplot as plt

# 1) load data
df = pd.read_csv("netflix_titles_nov_2019.csv")

# shape tells us how many rows and columns are in the dataset.
print("Dataset shape (rows, columns):", df.shape)
print("\n")

# head() shows the first 5 rows by default.
print("First 5 rows:")
print(df.head())
print("\n")

# info() shows column names, data types, and non-null counts.
print("Dataset info:")
print(df.info())
print("\n")

# isnull() returns True/False for each cell if value is missing.
# sum() then counts how many missing values each column has.
print("Missing values in each column:")
print(df.isnull().sum())
print("\n")

# dropna() removes rows with missing values.
# Here, we create a cleaned copy so original df stays unchanged.
df_clean = df.dropna(subset=["country", "cast", "date_added"])

print("Shape before cleaning:", df.shape)
print("Shape after dropna on country/cast/date_added:", df_clean.shape)
print("\n")

# unique() gives unique values from a column.
# We use it for the type column (usually Movie or TV Show).
print("Unique content types:")
print(df["type"].unique())
print("\n")

# value_counts() counts frequency of each category.
# Great for quick summaries.
print("Count of each content type:")
print(df["type"].value_counts())
print("\n")

# Filtering movies only.
movies_df = df[df["type"] == "Movie"]
print("Number of movies:", movies_df.shape[0])


# Filtering titles released in or after 2017.
recent_titles_df = df[df["release_year"] >= 2017]
print("Number of titles released in or after 2017:", recent_titles_df.shape[0])
print("\n")

# sort_values() sorts the DataFrame by a column.
# ascending=false means newest release years first.
sorted_by_year = df.sort_values(by="date_added", ascending=False)
print("Top 10 newest titles by date added:")
print(sorted_by_year[["title", "date_added"]].head(10))
print("\n")



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


# VISUALIZATIONS

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
country_counts.head(10).plot(kind="bar", color="#27d661")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()