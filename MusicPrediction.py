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
import pandas as pd 

#Filter Data
headers = ['id', 'song', 'artist', 'position', 'genre']
metadata = pd.read_csv("songs.csv", sep =';', header=0, names=headers)

#Drop columns 'id' and 'position'

metadata = metadata.drop('id', axis=1)
metadata = metadata.drop('position', axis=1)

#print(metadata.head)





