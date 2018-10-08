import media
import fresh_tomatoes

"""This module displays a web page with box art imagery
and a Youtube trailer for six movies"""


#Movies to be displayed on movie web page
star_wars = media.Movie("Star Wars - Return of the Jedi",
                        "The third and final episode of the orignal Star Wars trilogy",
                        "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                        "https://www.youtube.com/watch?v=5UfA_aKBGMc")

gladiator = media.Movie("Gladiator",
                        "Set in Roman times, the story of a once-powerful general forced to become a common gladiator",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=l-kV68xPVnM")

indiana_jones = media.Movie("Indiana Jones and the Last Crusade",
                            "Dr. Indiana Jones searches for the Holy Grail",
                            "https://upload.wikimedia.org/wikipedia/en/8/8c/Indiana_Jones_and_the_Last_Crusade.png",
                            "https://www.youtube.com/watch?v=a6JB2suJYHM")

airplane = media.Movie("Airplane!",
                       "A hilarious parody of the movie 'Airport 77'",
                       "https://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg",
                       "https://www.youtube.com/watch?v=qaXvFT_UyI8")

the_jerk = media.Movie("The Jerk",
                       "A man experiences one misadventure after another in an attempt to find himself",
                       "https://upload.wikimedia.org/wikipedia/en/3/3e/The_Jerk.jpg",
                       "https://www.youtube.com/watch?v=2Qut3v1KlSs")

the_mexican = media.Movie("The Mexican",
                          "A man travels to Mexico to retrieve a priceless antique pistol known as 'The Mexican'... or suffer the consequences",
                          "https://upload.wikimedia.org/wikipedia/en/1/14/Themexicanposter.jpg",
                          "https://www.youtube.com/watch?v=xfS4wPEIae0")


#List (array) of movies used as input to open_movies_page function in fresh_tomatoes.py
movies = [star_wars, gladiator, indiana_jones, airplane, the_jerk, the_mexican]

#Function to create and display movies on movie website
fresh_tomatoes.open_movies_page(movies)


