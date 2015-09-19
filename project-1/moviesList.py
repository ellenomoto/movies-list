import movies
import fresh_tomatoes
#import movies.py and fresh_tomatoes.py

#create a list to hold all Movie instances
moviesList = []
#create Movie instances and append each to the list

moviesList.append(movies.Movies("Rush Hour","http://ia.media-imdb.com/" + \
	"images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcwNjU3MTc0MQ@@._V1_SX6" + \
	"40_SY720_.jpg","https://www.youtube.com/watch?v=JMiFsFQcFLE",
	"When a Chinese diplomat's daughter is kidnapped in Los Angeles, he" + \
	" calls in Hong Kong Detective Inspector Lee (Jackie Chan) to assist" + \
	" the FBI with the case. But the FBI doesn't want anything to do with" + \
	" Lee, and they dump him off on the LAPD, who assign wisecracking " + \
	"Detective James Carter (Chris Tucker) to watch over him. Although " + \
	"Lee and Carter can't stand each other, they choose to work together" + \
	" to solve the case on their own when they figure out they've been " + \
	"ditched by both the FBI and police.", "Jackie Chan, Chris Tucker",
	"September 18, 1998", "6.9/10 IMDb"))
moviesList.append(movies.Movies("Titanic","http://www.cinemablend.com/" + \
	"images/news_gallery/n30500/titanic_13347771683736.jpg","https://" + \
	"www.youtube.com/watch?v=zCy5WQ9S4c0", "James Cameron's \"Titanic\"" + \
	" is an epic, action-packed romance set against the ill-fated maiden" + \
	" voyage of the R.M.S. Titanic; the pride and joy of the White Star " + \
	"Line and, at the time, the largest moving object ever built. She " + \
	"was the most luxurious liner of her era -- the \"ship of dreams\"" + \
	" -- which ultimately carried over 1,500 people to their death in" + \
	" the ice cold waters of the North Atlantic in the early hours of " + \
	"April 15, 1912.", "Kate Winslet, Leonardo DiCaprio","December 19, 1997", 
	"7.7/10 IMDb"))
moviesList.append(movies.Movies("Love Actually","https://upload.wikimedia" + \
	".org/wikipedia/en/e/eb/Love_Actually_movie.jpg","https://www.youtube" + \
	".com/watch?v=KdzH6a-XEGM",
	"Nine intertwined stories examine the complexities of the one emotion" + \
	" that connects us all: love. Among the characters explored are David" + \
	" (Hugh Grant), the handsome newly elected British prime minister who" + \
	" falls for a young junior staffer (Martine McCutcheon), Sarah (Laura" + \
	" Linney), a graphic designer whose devotion to her mentally ill " + \
	"brother complicates her love life, and Harry (Alan Rickman), a " + \
	"married man tempted by his attractive new secretary.",
	"Hugh Grant, Liam Neeson, Colin Firth, Laura Linney, Emma Thompson, " + \
	"Alan Rickman", "November 6, 2003", "7.7/10 IMDb"))
moviesList.append(movies.Movies("Because I Said So","http://www.gingle.in" + \
	"/watch/boxart/Because-I-Said-So.jpg","https://www.youtube.com/" + \
	"watch?v=gAZQDjlaRnk",
	"Daphne Wilder (Diane Keaton) is the proud mother of three women: " + \
	"Milly (Mandy Moore), Maggie (Lauren Graham) and Mae (Piper Perabo), " + \
	"and her love for her offspring knows no bounds. Because her youngest" + \
	", always chooses the wrong man, she decides to take action to " + \
	"prevent Milly from repeating the mistakes of the past. Dating " + \
	"disaster ensues when Daphne tries to achieve her goal by placing an " + \
	"online personal ad for Milly.", "Mandy Moore, Diane Keaton", 
	"February 2, 2007", "5.6/10 IMDb"))
moviesList.append(movies.Movies("The Blind Side","http://ia.media-imdb." + \
	"com/images/M/MV5BMjEzOTE3ODM3OF5BMl5BanBnXkFtZTcwMzYyODI4Mg@@._V1_" + \
	"SX640_SY720_.jpg","https://www.youtube.com/watch?v=gvqj_Tk_kuM",
	"Michael Oher (Quinton Aaron), a homeless black teen, has drifted " + \
	"in and out of the school system for years. Then Leigh Anne Tuohy " + \
	"(Sandra Bullock) and her husband, Sean (Tim McGraw), take him in. " + \
	"The Tuohys eventually become Michael's legal guardians, " + \
	"transforming both his life and theirs. Michael's tremendous " + \
	"size and protective instincts make him a formidable force on " + \
	"the gridiron, and with help from his new family and devoted tutor," + \
	" he realizes his potential as a student and football player.",
	"Sandra Bullock, Quinton Aaron", "November 20, 2009", "7.7/10 IMDb"))
moviesList.append(movies.Movies("Just Like Heaven","http://ecx.images-" + \
	"amazon.com/images/I/51KRTR6EH7L.jpg","https://www.youtube.com/" + \
	"watch?v=WPyJTNzzizw",
	"David (Mark Ruffalo) is a recently widowed architect moving into a " + \
	"new apartment in San Francisco. But the apartment isn't entirely " + \
	"empty; it's haunted by the ghost of a woman named Elizabeth (Reese " + \
	"Witherspoon). And although Elizabeth can't remember much about " + \
	"her life, she's convinced that she isn't really dead. While David " + \
	"recruits Darryl (Jon Heder), an absent-minded psychic, to get to " + \
	"the bottom of Elizabeth's identity, he and Elizabeth begin to " + \
	"fall in love.", "Reese Witherspoon, Mark Ruffalo", "September 16, 2005",
	"6.7/10 IMDb"))
moviesList.append(movies.Movies("Scream","http://images.moviepostershop." + \
	"com/scream-movie-poster-1996-1020271762.jpg","https://www.youtube." + \
	"com/watch?v=AWm_mkbdpCA",
	"The sleepy little town of Woodsboro just woke up screaming. " + \
	"There's a killer in their midst who's seen a few too many scary " + \
	"movies. Suddenly nobody is safe, as the psychopath stalks victims" + \
	", taunts them with trivia questions, then rips them to bloody " + \
	"shreds. It could be anybody...",
	"Neve Campbell, Courtney Cox, David Arquette", "December 20, 1996",
	"7.2/10 IMDb"))
moviesList.append(movies.Movies("I Know What You Did Last Summer","http:"+ \
	"//www.impawards.com/1997/posters/i_know_what_you_did_last_summer.jpg",
	"https://www.youtube.com/watch?v=EcWK0M4VMjA",
	"A year after killing vengeful hit-and-run victim Ben Wills " + \
	"(Muse Watson), who gutted her friends with an iron hook, " + \
	"college student Julie James (Jennifer Love Hewitt) is still " + \
	"shaken by the experience. When her roommate, Karla (Brandy), " + \
	"wins a vacation for four to the Bahamas, she plans to bring " + \
	"along her boyfriend, Tyrell (Mekhi Phifer), attractive Will " + \
	"(Matthew Settle) and Julie. At the resort, Julie starts receiving " + \
	"threatening notes and realizes Ben is still alive.",
	"Jennifer Love Hewitt, Sarah Michelle Gellar, Ryan Phillippe, " + \
	"Freddie Prinze Jr.", "October 17, 1997", "5.6/10 IMDb"))
moviesList.append(movies.Movies("Silence of the Lambs",
	"http://posterwire.com/wp-content/uploads/silence_of_the_lambs.jpg",
	"https://www.youtube.com/watch?v=RuX2MQeb8UM",
	"Jodie Foster stars as Clarice Starling, a top student at the FBI's" + \
	" training academy. Jack Crawford (Scott Glenn) wants Clarice to " + \
	"interview Dr. Hannibal Lecter (Anthony Hopkins), a brilliant " + \
	"psychiatrist who is also a violent psychopath, serving life behind " + \
	"bars for various acts of murder and cannibalism. Crawford believes " + \
	"that Lecter may have insight into a case and that Starling, as an "+ \
	"attractive young woman, may be just the bait to draw him out.",
	"Jodie Foster, Anthony Hopkins",
	"February 13, 1991",
	"8.6/10 IMDb"))

#use open_movies_page from fresh_tomatoes to create fresh_tomatoes.html
#fresh_tomatoes.html can be viewed in the browser
fresh_tomatoes.open_movies_page(moviesList)