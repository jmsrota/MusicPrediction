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

#Filter Data
headers = ['id', 'song', 'artist', 'position', 'genre']
metadata = pd.read_csv("songs.csv", sep =';', header=0, names=headers)

#Drop columns 'id' and 'position'

metadata = metadata.drop('id', axis=1)
metadata = metadata.drop('position', axis=1)

#Normalize the data

data = pd.DataFrame(metadata)

# lower case only for all attributes
data['song'] = data['song'].astype(str).str.lower()
data['artist'] = data['artist'].astype(str).str.lower()
data['genre'] = data['genre'].astype(str).str.lower()

# Remove special characters

data['song'] = data['song'].astype(str).str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
data['artist'] = data['artist'].astype(str).str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
data['genre'] = data['genre'].astype(str).str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

print(data[:3])

#MetaData format -> [song, artist, genre]

data['artist_genre'] = data['artist'] + " " + data['genre']

#Cosine Similarity 
#note -> make this work for 2D Arrays

vectorizer = CountVectorizer()



    


testProfile = ['The Killers rock']










