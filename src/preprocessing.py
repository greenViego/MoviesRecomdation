
def preprocess(movies, ratings):
    data = ratings.merge(movies, on='movieId')
    return data

