from media import Movie
import fresh_tomatoes

# Create individual Movie objects
toy_story = Movie("Toy Story",
                        81,
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")

avatar = Movie("Avatar",
                    162,
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

# Store Movie objects in a list
movies = [toy_story, avatar]

# Passing movies list to the open_movies_page function to render webpage
fresh_tomatoes.open_movies_page(movies)
