class Movies:
	#create class Movies which takes in arguments: title, poster url, youtube 
	#trailer url,
	def __init__(self, title, poster_image_url, trailer_youtube_url, 
		synopsis, actors, release_date, rating):
		#initialize class variables to input variables
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.synopsis = synopsis
		self.actors = actors
		self.release_date = release_date
		self.rating = rating

