import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

# === Download similarity.pkl from Google Drive ===
file_id = '1A7XZvyoyPmiA_2OD8-d_Yg-Jya4sG0HI'
output = 'similarity.pkl'

if not os.path.exists(output):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)

# 🔁 Load pickled data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# 📸 Function to fetch movie poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c532bcae9816a825d6f8d0def69a168e&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"

# 🤖 Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# 🌐 Streamlit UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Choose a movie:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # 🖼️ Display posters with names in 5 columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
