"""
This module contains the movie class that will be used in the
entertainment_center.py file
"""


class Movie():
    """
    Movie object is initialized below.

    title:
        should be the formal movie title as seen in IMDB
    art:
        needs to be the fully qualifed image address or url
        ex. "https://www.google.com/images/srpr/logo11w.png"
    trailer:
        needs to be the youtube watch link
        ex. "https://www.youtube.com/watch?v=u_CkKm7m6TM"
    director:
        should be a single name as listed in IMDB
    actors:
        can be list of no more than 3 actors/actresses as listed in IMDB
    release:
        must be the integer year in the following format 'yyyy'
    """

    def __init__(self, movie_title, director, poster_image,
                 trailer_youtube, actors, release):
        self.title = movie_title
        self.director = director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = actors
        self.release_date = release
