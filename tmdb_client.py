import requests
import random


api_token="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3YjU0OGUyZDE4NTA3ZTBkN2FhYzcyZWJlMGFlMTBiZiIsInN1YiI6IjYyNmZlOGM1ZDEzMzI0MTEzZTJjODFiNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.62L9nLRjTwwrgNq5pPcLrSJ8Pd3NaUEYcEPCYXidYpA"
headers = {
        "Authorization": f"Bearer {api_token}"
    }

def get_poster_url(_path, size="w342"):
    return f"https://image.tmdb.org/t/p/{size}/{_path}" 

def random_get_backdrop(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = requests.get(endpoint, headers=headers)
    backs = response.json()["backdrops"]
    chosen = random.choice(backs)
    print(chosen)
    return chosen

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_name):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many,kind="popular"):
    data = get_movies_list(kind)["results"]
    random.shuffle(data)
    return data[:how_many]