from src.data_loader import load_data
from src.content_based import train_content_model

# Step 1: Load data
movies, ratings = load_data()

# Step 2: Train and save similarity model
train_content_model(movies)