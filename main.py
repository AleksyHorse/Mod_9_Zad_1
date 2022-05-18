from flask import Flask, render_template, request
import requests

import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    types= ["now_playing","popular","upcoming","top_rated"]
    list_type = request.args.get('list_type', "popular")
    if list_type not in types:
        list_type="popular"
    movies = tmdb_client.get_movies(how_many=8, kind=list_type)
    return render_template("homepage.html", types=types, movies=movies, list_type=list_type)

@app.route("/home")
def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjU0OGUyZDE4NTA3ZTBkN2FhYzcyZWJlMGFlMTBiZiIsInN1YiI6IjYyNmZlOGM1ZDEzMzI0MTEzZTJjODFiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.62L9nLRjTwwrgNq5pPcLrSJ8Pd3NaUEYcEPCYXidYpA"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    det=tmdb_client.get_single_movie(movie_id)
    cast=tmdb_client.get_single_movie_cast(movie_id)[:8]
    picture = tmdb_client.random_get_backdrop(movie_id)
    return render_template("movie_details.html",cast=cast, movie=det, movie_id=movie_id, picture=picture)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

if __name__=="__main__":
    app.run(debug=True)