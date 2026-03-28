<<<<<<< HEAD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def train_content_model(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    movies['genres'] = movies['genres'].fillna('')
    
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    similarity = cosine_similarity(tfidf_matrix)

    pickle.dump(similarity, open('models/similarity.pkl', 'wb'))
    return similarity


def recommend(movie, movies, similarity):
    idx = movies[movies['title'] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

=======
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def train_content_model(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    movies['genres'] = movies['genres'].fillna('')
    
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    similarity = cosine_similarity(tfidf_matrix)

    pickle.dump(similarity, open('models/similarity.pkl', 'wb'))
    return similarity


def recommend(movie, movies, similarity):
    idx = movies[movies['title'] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

>>>>>>> 290880b (Fixed Altair compatibility issue)
    return [movies.iloc[i[0]].title for i in scores[1:6]]