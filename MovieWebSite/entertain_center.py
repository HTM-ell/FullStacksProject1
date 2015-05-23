import media
from fresh_tomatoes import open_movies_page as omp

toy_story = media.Movie("Toy Story",
						"www.youtube.com/watch?v=KYz2wyBy3kc")
						
avatar = media.Movie("Avatar",
					 "www.youtube.com/watch?v=cRdxXPV9GNQ")

sweeney_Todd = media.Movie("Sweeney Todd: The Demon Barber of Fleet Street",
						   "www.youtube.com/watch?v=_4R72KROZ20")
						   
pacific_Rim = media.Movie("Pacific Rim",
						  "www.youtube.com/watch?v=5guMumPFBag")

lion_king = media.Movie("The Lion King", "www.youtube.com/watch?v=4sj1MT05lAA")


fifth_element = media.Movie("The Fifth Element","www.youtube.com/watch?v=VkX7dHjL-aY")

movies = [toy_story, avatar, sweeney_Todd, pacific_Rim, lion_king, fifth_element]

omp(movies)
