<<<<<<< HEAD
<<<<<<< HEAD
def hybrid_recommend(movie, movies, similarity, matrix, model):
    from content_based import recommend
    from collaborative import recommend_cf

    cb = recommend(movie, movies, similarity)
    cf = list(recommend_cf(movie, matrix, model))

    return list(set(cb + cf))

from tmdb_model import recommend_tmdb

def hybrid_recommend(movie, movies, similarity, tmdb, tmdb_similarity):
    cb = recommend(movie, movies, similarity)
    tmdb_rec = recommend_tmdb(movie, tmdb, tmdb_similarity)

    return list(set(cb + tmdb_rec))
=======
=======
>>>>>>> 57de1a6da613f21fa4e9564ec2564e991543af35
def hybrid_recommend(movie, movies, similarity, matrix, model):
    from content_based import recommend
    from collaborative import recommend_cf

    cb = recommend(movie, movies, similarity)
    cf = list(recommend_cf(movie, matrix, model))

    return list(set(cb + cf))

from tmdb_model import recommend_tmdb

<<<<<<< HEAD
>>>>>>> 290880b (Fixed Altair compatibility issue)
=======
>>>>>>> 57de1a6da613f21fa4e9564ec2564e991543af35
