from Tkinter import Tk
from tkFileDialog import askopenfilename
import urllib


def select_file():
	Tk().withdraw() #pervents full TK GUI from displaying 
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	return(filename)

def read_text():
	quotes = open(select_file())
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()
	
read_text()