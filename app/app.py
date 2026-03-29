import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pickle
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.content_based import recommend

movies, ratings = load_data()
data = preprocess(movies, ratings)

similarity = pickle.load(open('models/similarity.pkl', 'rb'))

st.title("🎬 Movie Recommendation System")
from src.tmdb_model import load_tmdb, preprocess_tmdb, train_tmdb_model, recommend_tmdb
tmdb = load_tmdb()
tmdb = preprocess_tmdb(tmdb)
similarity, tmdb = train_tmdb_model(tmdb)

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    results = recommend_tmdb(selected_movie, tmdb, similarity)
    st.write("### Recommended Movies:")
    for movie in results:
        st.write(movie)

