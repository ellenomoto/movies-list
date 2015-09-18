import movies
import fresh_tomatoes
#import movies.py and fresh_tomatoes.py

#create a list to hold all Movie instances
moviesList = []
#create Movie instances and append each to the list
moviesList.append(movies.Movies("Rush Hour","http://ia.media-imdb.com/images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcwNjU3MTc0MQ@@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=JMiFsFQcFLE"))
moviesList.append(movies.Movies("Titanic","http://www.cinemablend.com/images/news_gallery/n30500/titanic_13347771683736.jpg","https://www.youtube.com/watch?v=zCy5WQ9S4c0"))
moviesList.append(movies.Movies("Love Actually","https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg","https://www.youtube.com/watch?v=KdzH6a-XEGM"))
moviesList.append(movies.Movies("Because I Said So","http://www.gingle.in/watch/boxart/Because-I-Said-So.jpg","https://www.youtube.com/watch?v=gAZQDjlaRnk"))
moviesList.append(movies.Movies("The Blind Side","http://ia.media-imdb.com/images/M/MV5BMjEzOTE3ODM3OF5BMl5BanBnXkFtZTcwMzYyODI4Mg@@._V1_SX640_SY720_.jpg","https://www.youtube.com/watch?v=gvqj_Tk_kuM"))
moviesList.append(movies.Movies("Just Like Heaven","http://ecx.images-amazon.com/images/I/51KRTR6EH7L.jpg","https://www.youtube.com/watch?v=WPyJTNzzizw"))
moviesList.append(movies.Movies("Scream","http://images.moviepostershop.com/scream-movie-poster-1996-1020271762.jpg","https://www.youtube.com/watch?v=AWm_mkbdpCA"))
moviesList.append(movies.Movies("I Know What You Did Last Summer","http://www.impawards.com/1997/posters/i_know_what_you_did_last_summer.jpg","https://www.youtube.com/watch?v=EcWK0M4VMjA"))
moviesList.append(movies.Movies("Silence of the Lambs","http://posterwire.com/wp-content/uploads/silence_of_the_lambs.jpg","https://www.youtube.com/watch?v=RuX2MQeb8UM"))

#use open_movies_page from fresh_tomatoes to create fresh_tomatoes.html
#fresh_tomatoes.html can be viewed in the browser
fresh_tomatoes.open_movies_page(moviesList)