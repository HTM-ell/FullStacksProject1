Synopsis

This project is to create a web application that act as a movie trailer library. Web page will display each movies title, poster image and plot. Once the movies poster image is clicked, a trailer for the movie will play.

Motivation

This project expands upon the final class room example for project 1 in Udacity coures. The initail code had the developer enter data manually for plot, title and poster image url. My code has refactored the initial solution by accessing an retriving data from the IMDb (Internet Movie Database)

Installation

Please install IMDbPy to allow this code to run properly 
site: http://imdbpy.sourceforge.net/downloads.html

Instructions
To add a new movie trailer to the library follow these steps:
1.Open entertain_center.py in IDLE 
2.Creative an instance of a movie object by defining a variable as media.Movie() and passing in the Title of the movie and a youtube url of the trailer. 
3. Add the created variable to the the movie array 
4. Run entertain_center.py
Example:

big_Hero_6 = media.Movie("Big Hero 6", **some youtube URL**)

movies = [..., ...., ...., ..., ..., big_Hero_6]

Run
