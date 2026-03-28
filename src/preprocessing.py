def preprocess(movies, ratings):
    data = ratings.merge(movies, on='movieId')
    return data

tmdb = tmdb_movies.merge(tmdb_credits, on='title')