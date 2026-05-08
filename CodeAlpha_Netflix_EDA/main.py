import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/netflix_titles.csv")

# Show first 5 rows
print(df.head())

# Basic information
print(df.info())

# Count Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.show()

# Top 10 countries
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# Ratings distribution
plt.figure(figsize=(10,5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title("Content Ratings Distribution")
plt.show()

# Release year trend
plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot()
plt.title("Netflix Content Release Trend")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.show()