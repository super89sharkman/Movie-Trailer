# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064
#when run the coce, init function is called, which will look for 4 piepces of input
import media
import fresh_tomatoes

the_dark_knight = media.Movie("The Dark Knight",
						# "When a vile criminal, the Joker, throws the town into chaos, Batman finds himself treading a fine line between heroism and vigilantism",
						"https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
						"https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
						"http://www.rottentomatoes.com/m/the_dark_knight/")


the_dark_knight_rises = media.Movie("The Dark Knight Rises",
					 # "Bane forces Batman out into a battle he may not be able to win",
					 "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
					 "https://www.youtube.com/watch?v=g8evyE9TuYk",
					 "http://www.rottentomatoes.com/m/the_dark_knight_rises/")

the_revenant = media.Movie("The Revenant", 
							# "A frontierman is left for dead, he must find his way through the snowy terrain to find the man who betrays him", 
							"https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
							"https://www.youtube.com/watch?v=LoebZZ8K5N0",
							"http://www.rottentomatoes.com/m/the_revenant_2015/")


wolf_of_wallstreet = media.Movie("The Wolf of Wallstreet", 
							# "A young broker makes a huge fortune by defrauding wealthy investors", 
							"https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
							"https://www.youtube.com/watch?v=iszwuX1AK6A",
							"http://www.rottentomatoes.com/m/the_wolf_of_wall_street_2013/")

django_unchained = media.Movie("Django Unchained", 
							# "A former slave seeks to rescue his wife in the infamous plantation of Calvin Candie", 
							"https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
							"https://www.youtube.com/watch?v=0fUCuvNlOCg",
							"http://www.rottentomatoes.com/m/django_unchained_2012/")


# movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)
# the_revenant.show_trailer()
movies = [the_dark_knight, the_dark_knight_rises, the_revenant, wolf_of_wallstreet, django_unchained]
# # rataouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.valid_ratings)
