import imdb

class IMDbInfo():
        
        def __init__(self,movie_title):
                ia = imdb.IMDb()
                self.movie= ia.get_movie(ia.search_movie(movie_title)[0].movieID)
		
        def plot(self):
                return self.movie.get('plot')[0]
        def poster_image(self):
                return self.movie.get('cover url')
        def title(self):
                return self.movie.get('title')
