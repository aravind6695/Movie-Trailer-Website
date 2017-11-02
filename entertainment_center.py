from media import Movie
import fresh_tomatoes
import urllib
import json


def get_movie(tmdb_id):
    """Returns a Movie object given the TMDb ID of a movie.

    Args:
        tmdb_id (str): The unique ID for a movie on the TMDb website.

    Returns:
        An object of class Movie.
    """

    # TMDb API key
    api_key = "a67cb6ea86667935513fc0b0e51f0d1e"

    # Retrieve movie information
    url = ("https://api.themoviedb.org/3/movie/" + tmdb_id +
           "?api_key=" + api_key)
    movie = json.load(urllib.urlopen(url))
    title = movie['original_title']
    duration = movie['runtime']
    overview = movie['overview']
    poster_image_url = "http://image.tmdb.org/t/p/w1920" + movie['poster_path']

    # Retrieve YouTube trailer URL
    url = ("https://api.themoviedb.org/3/movie/" + tmdb_id +
           "/videos?api_key=" + api_key)
    movie = json.load(urllib.urlopen(url))
    trailer_youtube_url = ("https://www.youtube.com/watch?v=" +
                           movie['results'][0]['key'])

    # Return a movie object for the given movie
    return Movie(title, duration, overview, poster_image_url,
                 trailer_youtube_url)


# Create Movie objects using the get_movie() function
the_dark_knight = get_movie("155")
the_godfather = get_movie("238")
the_shawshank_redemption = get_movie("278")
interstellar = get_movie("157336")
inception = get_movie("27205")
dunkirk = get_movie("374720")

# Store Movie objects in a list
movies = [
    the_dark_knight,
    the_godfather,
    the_shawshank_redemption,
    interstellar,
    inception,
    dunkirk,
]

# Passing movies list to the open_movies_page() function to render webpage
fresh_tomatoes.open_movies_page(movies)
