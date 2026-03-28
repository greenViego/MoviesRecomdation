import pickle

# import your functions
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.content_based import recommend  # or wherever similarity is created

# Step 1: Load data
movies, ratings = load_data()

# Step 2: Preprocess
processed_data = preprocess(movies, ratings)

# Step 3: Generate similarity matrix
similarity = recommend(processed_data)  # or your actual function

# Step 4: Save model
pickle.dump(similarity, open('models/similarity.pkl', 'wb'))

print("✅ similarity.pkl saved successfully!")