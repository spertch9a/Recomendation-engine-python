import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing data
userrating_df = pd.read_csv("user_ratings.csv")
# Inspect the listening_history_df DataFrame
print(userrating_df.head())

# finding the most popular items
print("finding the most popular items")
userrating_df['title'].value_counts()


# Calculate the number of unique values
print(userrating_df[['rating']].nunique())

# Display a histogram of the values in the Rating column
userrating_df['rating'].hist()
# activate this to show the plot
# plt.show()

# Finding the most liked items
print("Average rating for each movie")
avg_rating_df = userrating_df[["title", "rating"]].groupby(['title']).mean()
print(avg_rating_df.head())

# here we note that they are not sorted, we'll sort them then
sorted_avg_rating_df = avg_rating_df.sort_values(by='rating', ascending=False)
print("Sorted")
print(sorted_avg_rating_df.head())

# now we note that some movies have been sorted at first and they're not know,
# a movie with one good review has a solid chance to be sorted as one of the best movies

# calculating the book frequency
movie_frequency = userrating_df["title"].value_counts()
print(movie_frequency)

# we'll take the indexes of the frequently reviewed movies
frequently_reviewed_movies = movie_frequency[movie_frequency > 100].index
print(frequently_reviewed_movies)

# taking a subset of the movies that are frequent, using the isin function
frequent_movies_df = userrating_df[userrating_df["title"].isin(
    frequently_reviewed_movies)]

# this subset will be used to show the highest books ratings on average
frequent_movies_avgs = frequently_reviewed_movies[[
    "title", "rating"]].groupby("title").mean()
print(frequent_movies_avgs.sort_values(by="rating", ascending=False).head())


# Get the counts of occurrences of each movie title
movie_popularity = userrating_df["title"].value_counts()

# Inspect the most common values
print(movie_popularity.head().index)

# Find the mean of the ratings given to each title
average_rating_df = userrating_df[["title", "rating"]].groupby('title').mean()

# Order the entries by highest average rating to lowest
sorted_average_ratings = average_rating_df.sort_values(
    by="rating", ascending=False)

# Inspect the top movies
print(sorted_average_ratings.head())
