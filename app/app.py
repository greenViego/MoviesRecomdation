import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

# Import TMDB pipeline
from src.tmdb_model import (
    load_tmdb,
    preprocess_tmdb,
    train_tmdb_model,
    recommend_tmdb
)

# Title
st.title("🎬 Movie Recommendation System")

# Load and preprocess data
tmdb = load_tmdb()
tmdb = preprocess_tmdb(tmdb)

# Train model (creates similarity matrix)
similarity, tmdb = train_tmdb_model(tmdb)

# Movie selection dropdown
movie_list = tmdb['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

# Recommendation button
if st.button("Recommend"):
    results = recommend_tmdb(selected_movie, tmdb, similarity)

    st.write("### Recommended Movies:")
    for movie in results:
        st.write(f"👉 {movie}")