import imdb
	
	ia = imdb.IMDb()
	movie = ''
	
	def movieID(movie_title):
		movie = ia.get_movie(ia.search_movie(movie_title)[0].movieID)
		
	def plot():
		return movie.get('plot')[0]

	def poster_image()
		return movie.get('cover url')