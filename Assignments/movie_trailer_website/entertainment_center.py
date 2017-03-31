"""
list of movies that feed into fresh_tomatoes.py file

"""


import media
import fresh_tomatoes


THE_IMITATION_GAME = media.Movie("The Imitation Game",
                                 "Morten Tyldum",
                                 "https://upload.wikimedia.org/"
                                 "wikipedia/en/5/5e/"
                                 "The_Imitation_Game_poster.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM",
                                 "BenedictCumberbatchKeiraKnightley",
                                 2015)

THE_MAN_WHO_KNEW_INFINITY = media.Movie("The Man Who Knew Infinity",
                                        "Matthew Brown",
                                        "https://upload.wikimedia.org/"
                                        "wikipedia/en/thumb/d/d8/"
                                        "The_Man_Who_Knew_Infinity"
                                        "_%28film%29.jpg/"
                                        "220px-The_Man_Who_Knew_Infinity_"
                                        "%28film%29.jpg",
                                        "https://www.youtube.com/"
                                        "watch?v=RH3OxVFvTeg",
                                        "Dev Patel,Jeremy Irons",
                                        2014)

A_BEAUTIFUL_MIND = media.Movie("A Beautiful Mind", "Ron Howard",
                               "https://upload.wikimedia.org/"
                               "wikipedia/en/thumb/b/b8/"
                               "A_Beautiful_Mind_Poster.jpg/"
                               "220px-A_Beautiful_Mind_Poster.jpg",
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o",
                               "Russell Crowe, Jennifer Connelly",
                               2001)

NUMBER_23 = media.Movie("The Number 23", "Joel Schumacher",
                        "https://upload.wikimedia.org/wikipedia/"
                        "en/thumb/c/cc/Number23.jpg/220px-Number23.jpg",
                        "https://www.youtube.com/watch?v=W1PeQJzoxVM",
                        "Jim Carrey,Virginia Madsen", 2007)
GRAMS_21 = media.Movie("21 Grams", "Alejandro Gonzalez",
                       "https://upload.wikimedia.org/wikipedia/"
                       "en/thumb/7/74/21_grams_movie.jpg/"
                       "220px-21_grams_movie.jpg",
                       "https://www.youtube.com/watch?v=FZXR9ZrRR2c",
                       "Naomi Watts,Sean Penn", 2003)

THE_OXFORD_MURDER = media.Movie("The Oxford Murder", "Alex de la Iglesia",
                                "https://upload.wikimedia.org/wikipedia/"
                                "en/thumb/0/07/The_Oxford_Murders_poster.jpg/"
                                "220px-The_Oxford_Murders_poster.jpg",
                                "https://www.youtube.com/watch?v=V8edqqoXcg4",
                                " Elijah Wood,John Hurt", 2008)
movies = [A_BEAUTIFUL_MIND,
          THE_IMITATION_GAME,
          THE_MAN_WHO_KNEW_INFINITY,
          GRAMS_21, NUMBER_23,
          THE_OXFORD_MURDER]
fresh_tomatoes.open_movies_page(movies)
