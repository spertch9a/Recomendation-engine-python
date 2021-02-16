# https://www.analyticsvidhya.com/blog/2020/11/create-your-own-movie-movie-recommendation-system/
#  We will be using an item-based collaborative filtering algorithm for our purpose.


#getting the data up and running
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("user_ratings.csv")
print(movies.head())
print(ratings.head())


final_dataset = ratings.pivot(index='movieId',columns='userId',values='rating')

print(final_dataset.head())