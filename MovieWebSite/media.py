import webbrowser
import refine

class Movie():
        # about this module     http://imdbpy.sourceforge.net/docs/README.package.txt
        
        
        def __init__(self, movie_title, trailer_youtube):
                movie = refine.IMDbInfo(movie_title)
                self.title = movie.title()
                self.storyline = movie.plot()
                self.poster_image_url = movie.poster_image()
                self.trailer_youtube_url =trailer_youtube
                
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
                
        
