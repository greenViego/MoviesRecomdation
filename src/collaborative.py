from sklearn.neighbors import NearestNeighbors
import pickle

def train_cf_model(data):
    matrix = data.pivot_table(index='userId', columns='title', values='rating').fillna(0)

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(matrix)

    pickle.dump(model, open('models/knn_model.pkl', 'wb'))
    return model, matrix


def recommend_cf(movie, matrix, model):
    movie_vec = matrix[movie].values.reshape(1, -1)
    distances, indices = model.kneighbors(movie_vec, n_neighbors=6)

    return matrix.columns[indices.flatten()[1:]]