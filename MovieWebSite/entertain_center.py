import media
from fresh_tomatoes import open_movies_page as omp

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_aa.jpg",
						"www.youtube.com/watch?v=KYz2wyBy3kc")
						
avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://khabinh.vn/images/files/avatar-oridginal.jpg",
					 "www.youtube.com/watch?v=cRdxXPV9GNQ")

sweeney_Todd = media.Movie("Sweeney Todd: The Demon Barber of Fleet Street",
						   "story of Benjamin Barker, alias Sweeney Todd, who returns to London after 15 years'" +
						   "transportation on trumped-up charges, to take revenge on the judge who banished him",
						   "http://ia.media-imdb.com/images/M/MV5BMTg3NjUxMzM5NV5BMl5BanBnXkFtZTcwMzQ1NjQzMw@@._V1_SX640_SY720_.jpg",
						   "www.youtube.com/watch?v=_4R72KROZ20")
						   
pacific_Rim = media.Movie("Pacific Rim",
						  "a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon",
						  "http://vignette2.wikia.nocookie.net/pacificrim/images/2/27/Postery06u.jpg/revision/latest?cb=20130728052931",
						  "www.youtube.com/watch?v=5guMumPFBag")
						  
movies = [toy_story, avatar, sweeney_Todd, pacific_Rim]

omp(movies)
