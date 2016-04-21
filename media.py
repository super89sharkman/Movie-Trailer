# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    # This class provides a way to store movie related information
    # valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, poster_image, trailer_youtube, review):
        # initialize instance of class Movie
        #iniailizees spaces in memory, self- is object being created
        #init to initalize information to remember in class
        self.title = movie_title
        #self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.review_url= review

    def show_trailer(self):
        #opens browser link to trailer page
    	webbrowser.open(self.trailer_youtube_url)


