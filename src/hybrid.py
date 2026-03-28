def hybrid_recommend(movie, movies, similarity, matrix, model):
    from content_based import recommend
    from collaborative import recommend_cf

    cb = recommend(movie, movies, similarity)
    cf = list(recommend_cf(movie, matrix, model))

    return list(set(cb + cf))

from tmdb_model import recommend_tmdb

