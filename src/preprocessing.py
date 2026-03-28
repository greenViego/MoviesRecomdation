<<<<<<< HEAD
def preprocess(movies, ratings):
    data = ratings.merge(movies, on='movieId')
    return data

=======
def preprocess(movies, ratings):
    data = ratings.merge(movies, on='movieId')
    return data

>>>>>>> 290880b (Fixed Altair compatibility issue)
tmdb = tmdb_movies.merge(tmdb_credits, on='title')