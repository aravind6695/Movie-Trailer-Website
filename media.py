class Video():
    """This class stores video information."""

    def __init__(self, title, duration):
        """Initiliazes a Video object with the given arguments.

        Args:
            title (str): The title of the video.
            duration (int): The duration(length) of the video.
        """
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class stores movie information."""

    def __init__(self, title, duration, storyline, poster_image_url,
                 trailer_youtube_url):
        """Initiliazes a Movie object with the given arguments.

        Args:
            title (str): The title of the movie.
            duration (int): The duration(length) of the movie.
            storyline (str): A short overview of the movie.
            poster_image_url (str): The URL for a poster image.
            trailer_youtube_url (str): The URL for a trailer on YouTube.
        """
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
