"""
Music Prediction using an HTML platform to run

Song Recommendation based on text

Research Required:

- I need to know the layout for the program -> where to start, how the app will work
- I need to know which algorithm to use
- I need to know how to connect it to a webpage
- I need to know if I want to use language recognition
- I need to find plug-ins/imports to use for the AI -> How to use properly
- I need to get a music library for the AI

Steps: 

Data Collection -> Song metaData (Genre, artist, etc)

Data Preprocessing -> Handle missing data, normalization, encoding (one-hot vector)

Feature Selection -> Which features are important

Algorithm -> Content-based filtering

Model Training -> Split into testing and training

Evaluate model -> Check the accuracy of the model

Deployment -> Connect AI to HTML

Date Created: Mon Oct 21, 2024
Last Modified: Mon Oct 21, 2024

Author: James Rota

"""

# Imports -> What does the AI need. 

#import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import Functions
import pandas as pd
import numpy as np 
import re


#test Functions:

# vector1 = [3, 2, 3, 1]
# vector2 = [2, 1, 0, 1]

# result = Functions.cosine_Similarity(vector1, vector2)
# print("testing functions from file:", result)

def music_recommender(user):
    #Filter Data
    headers = ['id', 'song', 'artist', 'position', 'genre']
    metadata = pd.read_csv("/Users/jamesrota/Vulnerability_Scanner/Vulnerability_Scanner_Web_APP/application/csv/songs.csv", sep =';', header=0, names=headers)

    #Drop columns 'id' and 'position'

    metadata = metadata.drop('id', axis=1)
    metadata = metadata.drop('position', axis=1)

    #Normalize the data

    data = pd.DataFrame(metadata)

    data['artist'] = data['artist'].astype(str).str.lower().str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    data['genre'] = data['genre'].astype(str).str.lower().str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    data['song'] = data['song'].astype(str).str.lower().str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
    data['unique_id'] = data['song'] + ' - ' + data['artist'] + ' - ' + data['genre']

    # Drop duplicate rows based on the unique identifier
    data_unique = data.drop_duplicates(subset='unique_id')

    #MetaData format -> [song, artist, genre]

    #Cosine Similarity 
    #note -> make this work for 2D Arrays

    data_unique['combined_features'] = data_unique['song'] + ' ' + data_unique['artist'] + ' ' + data_unique['genre']

    vectorizer = CountVectorizer()

    feature_matrix_database = vectorizer.fit_transform(data_unique['combined_features'])

    feature_matrix_user = vectorizer.transform(user)

    similiarities = cosine_similarity(feature_matrix_database, feature_matrix_user).flatten()

    top_songs_indices = np.argsort(similiarities)[::-1][:5]

    recommended_songs = data.iloc[top_songs_indices][['artist', 'song']]

    return recommended_songs













