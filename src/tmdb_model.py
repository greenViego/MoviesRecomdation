<<<<<<< HEAD
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_tmdb():
    movies = pd.read_csv('data/tmdb_5000_movies.csv')
    credits = pd.read_csv('data/tmdb_5000_credits.csv')
    return movies.merge(credits, on='title')


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


def get_cast(text):
    L = []
    for i in ast.literal_eval(text)[:3]:
        L.append(i['name'])
    return L


def get_director(text):
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            return i['name']


def preprocess_tmdb(tmdb):
    tmdb = tmdb[['title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

    tmdb['genres'] = tmdb['genres'].apply(convert)
    tmdb['keywords'] = tmdb['keywords'].apply(convert)
    tmdb['cast'] = tmdb['cast'].apply(get_cast)
    tmdb['crew'] = tmdb['crew'].apply(get_director)

    tmdb['overview'] = tmdb['overview'].fillna('')

    tmdb['tags'] = tmdb['overview'] + " " + \
                   tmdb['genres'].apply(lambda x: " ".join(x)) + " " + \
                   tmdb['keywords'].apply(lambda x: " ".join(x)) + " " + \
                   tmdb['cast'].apply(lambda x: " ".join(x)) + " " + \
                   tmdb['crew']

    return tmdb


def train_tmdb_model(tmdb):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(tmdb['tags']).toarray()

    similarity = cosine_similarity(vectors)
    return similarity


def recommend_tmdb(movie, tmdb, similarity):
    idx = tmdb[tmdb['title'] == movie].index[0]
    distances = similarity[idx]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

=======
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_tmdb():
    movies = pd.read_csv('data/tmdb_5000_movies.csv')
    credits = pd.read_csv('data/tmdb_5000_credits.csv')
    return movies.merge(credits, on='title')


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


def get_cast(text):
    L = []
    for i in ast.literal_eval(text)[:3]:
        L.append(i['name'])
    return L


def get_director(text):
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            return i['name']


def preprocess_tmdb(tmdb):
    tmdb = tmdb[['title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

    tmdb['genres'] = tmdb['genres'].apply(convert)
    tmdb['keywords'] = tmdb['keywords'].apply(convert)
    tmdb['cast'] = tmdb['cast'].apply(get_cast)
    tmdb['crew'] = tmdb['crew'].apply(get_director)

    tmdb['overview'] = tmdb['overview'].fillna('')

    tmdb['tags'] = tmdb['overview'] + " " + \
                   tmdb['genres'].apply(lambda x: " ".join(x)) + " " + \
                   tmdb['keywords'].apply(lambda x: " ".join(x)) + " " + \
                   tmdb['cast'].apply(lambda x: " ".join(x)) + " " + \
                   tmdb['crew']

    return tmdb


def train_tmdb_model(tmdb):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(tmdb['tags']).toarray()

    similarity = cosine_similarity(vectors)
    return similarity


def recommend_tmdb(movie, tmdb, similarity):
    idx = tmdb[tmdb['title'] == movie].index[0]
    distances = similarity[idx]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

>>>>>>> 290880b (Fixed Altair compatibility issue)
    return [tmdb.iloc[i[0]].title for i in movies_list]