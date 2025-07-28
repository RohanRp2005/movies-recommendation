# movies-recommendation
# 🎬 Movie Recommendation System

Hi! This is a simple machine learning-based movie recommender system. You just select a movie, and it will recommend 5 similar movies along with their posters!

I built this project as part of my learning journey using Python, Jupyter Notebook, and Streamlit.

---

## 🔍 What It Does

- You choose a movie from the dropdown.
- It uses a similarity model to find 5 most similar movies.
- It fetches the movie posters from TMDB and shows them with names.

---

## 🛠 Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn (for similarity calculation)
- Pickle (to save the model)
- TMDB API (for movie posters)
- Streamlit (for web app)
- Jupyter Notebook (for training and preprocessing)

---

## 📦 Files in the Repo

- `app.py` → main Streamlit web app
- `movies_dict.pkl` → dictionary of all movie info
- `similarity.pkl` → similarity matrix (precomputed)
- `requirements.txt` → list of required Python libraries

---

## 📌 How to Run

1. Clone the repository
2. Install the libraries using `pip install -r requirements.txt`
3. Run the app with:
   ```bash
   streamlit run app.py

   
## 🌐 Live App
👉 [Try the app here](https://rpmoviesrecco.streamlit.app/)
