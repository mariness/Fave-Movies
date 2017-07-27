import fresh_tomatoes
import media

#This shows movie title, movie image, and video

book_of_life = media.Movie(
    "The Book of Life",
    "A boy is torn between following his heart or fullfilling family traditions",
    "https://upload.wikimedia.org/wikipedia/en/6/61/The_Book_of_Life_%282014_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=NBw5YScs8iQ")
fifty_first_dates = media.Movie(
    "50 First Dates",
    "A romantic comedy on how a guy makes a girl with short term memory loss fall in love with him everyday",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/50FirstDates.jpg",
    "https://www.youtube.com/watch?v=ErjP5xMTc8I")
hook = media.Movie(
    "Hook",
    "Grown up Peter Pan comes back to Neverland",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/Hook_poster_transparent.png",
    "https://www.youtube.com/watch?v=y98AuG2-yU4")
independence_day = media.Movie(
    "Independence Day",
    "Aliens attack the earth and the people come together to defend it",
    "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
    "https://www.youtube.com/watch?v=xr7Zy9l13y0")
oceans_eleven = media.Movie(
    "Ocean's Eleven",
    "A group of guys orchestrate a heist to steal money from a prosperous casino",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
    "https://www.youtube.com/watch?v=u7VTkceSsEw&hl=es_ES&fs=1&")
inception = media.Movie(
    "Inception",
    "A theif implants an idea into the mind of a CEO for corporate espionage",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM")


movies = [book_of_life, fifty_first_dates, hook, independence_day, oceans_eleven, inception]
fresh_tomatoes.open_movies_page(movies)

