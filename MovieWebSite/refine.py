#This module handles all Internet Movie Database quries and refinements of searchs

#import the imdb module
import imdb # about this module http://imdbpy.sourceforge.net/docs/README.package.txt

#define the class for this module
class IMDbInfo():

        #initilize: accept movie title. Creates an instance of the IMDB class
        #searches database for the movie ID by title retrives first key and sets
        #as self.movie
        def __init__(self,movie_title):
                ia = imdb.IMDb()
                #defines a movie object that has several keys associated with it
                self.movie= ia.get_movie(ia.search_movie(movie_title)[0].movieID)

	#returns the first key from the plot qury of the imdb database
        def plot(self):
                return self.movie.get('plot')[0]
        
        #returns the poster image associated with the movie ID defined init
        def poster_image(self):
                return self.movie.get('cover url')

        #returns movie title associated with the movie ID 
        def title(self):
                return self.movie.get('title')
