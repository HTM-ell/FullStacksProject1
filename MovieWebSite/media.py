import webbrowser
import refine #imports module I created to interact with imdb

class Movie():
        
        #This has been refactored fromt the original code to only need two arguments
        #To be supplied to the init
        def __init__(self, movie_title, trailer_youtube):
                #Creates an instance of the refine.IMDbInfo Class
                movie = refine.IMDbInfo(movie_title)
                self.title = movie.title()
                self.storyline = movie.plot()
                self.poster_image_url = movie.poster_image()
                self.trailer_youtube_url =trailer_youtube
                
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
                
        
