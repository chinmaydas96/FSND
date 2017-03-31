import media
import fresh_tomatoes


power_rangers = media.Movie("Power Rangers", "Five ordinary teens must become"
                        "something extraordinary and their world is on"
                        "the verge of being obliterated by an alie"
                        "threat.", "https://s6.postimg.org/oosffvqdt/power.jpg",
                        "https://www.youtube.com/watch?v=5kIe6UZHSXw")

logan = media.Movie("Logan", "In future,Logan cares for an ailing Professor X"
                    "at a remote outpost somewhere. while hiding from "\
                    "they meets a young mutant who is very much like"\
                    "  Logan. Logan must now protect the girl from "\
                    "those dark force that want to capture her.",
                    "https://s6.postimg.org/ffq95rhht/logan.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")


# movies = [power_rangers,logan]
# fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__doc__)