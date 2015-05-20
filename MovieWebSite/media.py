import webbrowser
import refine

class Movie():
	# about this module	http://imdbpy.sourceforge.net/docs/README.package.txt
	
	
	def __init__(self, movie_title, trailer_youtube):
		movieID = refine.movieID(movie_title)
		self.title = refine.title()
		self.storyline = refine.plot()
		self.poster_image_url = refine.poster_image()
		self.trailer_youtube_url =trailer_youtube
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		
	