<<<<<<< HEAD
<<<<<<< HEAD
def preprocess(movies, ratings):
    data = ratings.merge(movies, on='movieId')
    return data

=======
=======
>>>>>>> 57de1a6da613f21fa4e9564ec2564e991543af35
def preprocess(movies, ratings):
    data = ratings.merge(movies, on='movieId')
    return data

<<<<<<< HEAD
>>>>>>> 290880b (Fixed Altair compatibility issue)
=======
>>>>>>> 57de1a6da613f21fa4e9564ec2564e991543af35
tmdb = tmdb_movies.merge(tmdb_credits, on='title')