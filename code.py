from imdb import Cinemagoer
from thefuzz import fuzz

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
#movie = ia.search_movie("THE MATRIX")[0]
# print(movie.movieID)

# get the fifth movie review


def movie_review():
    movie_reviews = ia.get_movie_reviews('0133093')
    print(movie_reviews['data']['reviews'][4]['content'])


movie_review()

# get movie score


def movie_score():
    movie_score = ia.get_movie('0133093')
    movie_rating = movie_score['rating']
    print(f'This movie is rating {movie_rating}')


movie_score()

# taglines of the movie


def tag():
    movie = ia.get_movie('0133093', info=['taglines'])
    movie.infoset2keys
    {'taglines': ['taglines']}
    print(movie.get('taglines')[1:5])


tag()

# is there any critics?


def critics():
    movie = ia.get_movie('0133093', info=['critic reviews'])
    movie.infoset2keys
    {'critic reviews': ['critic reviews']}
    print(movie.get('critic reviews'))


critics()

# genre of the movie


def genre():
    movie = ia.get_movie('0133093')
    genre = movie['genre']
    print(f'The genre of this movie is {genre}')


genre()

# what are the top 10 movies


def top_10():
    top = ia.get_top250_movies()
    top_10 = top[0:9]
    print(f'Top 10 movies are {top_10}')


top_10()

# what are the bottom 10 movies


def bot_10():
    bot = ia.get_bottom100_movies()
    bot_10 = bot[0:9]
    print(f'Bottom 10 movies are {bot_10}')


bot_10()

# What movies do this actor in


def actor():
    movie = ia.get_movie('0133093')
    actor = movie['cast'][0]
    print(actor['name'])


actor()


def actor_movie():

    actor = ia.get_person('0000206')
    for job in actor['filmography'].keys():
        print('# Job: ', job)
    for movie in actor['filmography'][job]:
        print(movie['title'])


actor_movie()


# Text similarity
def movie_review_score():
    movie_reviews = ia.get_movie_reviews('0133093')
    movie_reviews1 = movie_reviews['data']['reviews'][10]['content']
    movie_reviews2 = movie_reviews['data']['reviews'][3]['content']


movie_review_score()
score = fuzz.ratio('movie_reviews1', 'movie_reviews2')
print(score)


def main():
    movie_review()
    movie_score()
    movie_score()
    tag()
    critics()
    genre()
    top_10()
    bot_10()
    actor()
    actor_movie()
    movie_review_score()

if __name__ == "__main__":
    main()

#code reference: 'https://buildmedia.readthedocs.org/media/pdf/imdbpy/stable/imdbpy.pdf'