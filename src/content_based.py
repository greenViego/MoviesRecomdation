from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def train_content_model(movies):
    
    
    movies = movies.head(2000)

    # Clean data
    movies['genres'] = movies['genres'].fillna('')
    
    
    cv = CountVectorizer(max_features=1500, stop_words='english')
    
    vectors = cv.fit_transform(movies['genres']).toarray()
    
    similarity = cosine_similarity(vectors)

    import pickle
    pickle.dump(similarity, open('models/similarity.pkl', 'wb'))

    print("✅ similarity.pkl saved successfully!")

    return similarity


def recommend(movie, movies, similarity):
    idx = movies[movies['title'] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return [movies.iloc[i[0]].title for i in scores[1:6]]