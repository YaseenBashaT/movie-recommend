# recommendation.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from rapidfuzz import process, fuzz

# Load data
movies = pd.read_csv('data/movie.csv')
ratings = pd.read_csv('data/rating.csv')

# Process data
movie_titles = movies['title']
movie_genres = movies['genres']  

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movie_genres)

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Get recommendations

def recommend_movie(title):
    if title not in movie_titles.values:
        return pd.Series([])  # Return an empty Series if the title is not found

    idx = movie_titles[movie_titles == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Exclude the first item which is the movie itself
    movie_indices = [i[0] for i in sim_scores]
    
    return movies['title'].iloc[movie_indices].tolist()  # Return a list instead of Series
def get_suggestions(query):
    # Filter movies based on the query for suggestions
    suggestions = movies[movies['title'].str.contains(query, case=False, na=False)]
    suggestions_list = suggestions['title'].tolist()
    return suggestions_list