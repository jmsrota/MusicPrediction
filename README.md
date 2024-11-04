# Music Receommender System

## Overview

This project implements a Music Recommender System using Python libraries such as scikit-learn and pandas. 
The system reads song data from a CSV file, processes and normalizes it, 
and uses cosine similarity to recommend songs based on user input.

## Prerequisites 

- Python
- Skikit-learn
- Numpy
- Pandas

## Project Structure

-main.py: Contains the music_recommender function, which processes the input and provides top 5 song recommendations.
-songs.csv: A CSV file containing song metadata with the following columns: id, song, artist, position, and genre.

## How it Works

1. Data Loading:
   The function reads song data from a CSV file.

2. Data Preprocessing:
   The id and position columns are removed as they are not relevant for recommendations.
   The data is normalized by converting all text to lowercase and removing special characters to ensure uniformity.
   A unique identifier is created by combining the song, artist, and genre columns, allowing duplicate entries to be removed.
   
4. Feature Extraction:
   A combined_features column is created by concatenating song, artist, and genre data.
   The CountVectorizer from scikit-learn is used to create a feature matrix for both the database and user input.
   
4. Similarity Calculation:
   The cosine_similarity function is used to compute the similarity between the user input and the database.
   The top 5 most similar songs are selected and returned.

## Usage

### Example code:

user_input = ["song name by artist in genre"]

recommendations = music_recommender(user_input)

print(recommendations)

## License

This project is open-source
