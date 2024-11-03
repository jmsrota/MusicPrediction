from application import app
from flask import render_template, request
import requests
from .MusicPrediction import music_recommender

@app.route('/')
@app.route('/Music_Suggestions')
def Music_Suggestions():
   return render_template("Sample.html")


@app.route('/music' , methods = ['GET' , 'POST'])
def music():
   user_input = str(request.form["url"])

   user_input = [user_input]
   recommended_songs = music_recommender(user_input)
   recommended_songs_list = recommended_songs[['song', 'artist']].to_dict(orient='records')
   return render_template('Sample.html', recommended_songs_list=recommended_songs_list)

if __name__ == '__main__':
    app.run()