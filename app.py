import streamlit as st
import pickle
import requests
import pandas as pd

# Load the movie data and similarity matrix from pickle files
movies_dict = pickle.load(open('datas.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    # Find the index of the selected movie in the dataset
    movie_index = movies[movies['title'] == movie].index[0]

    # Get the similarity scores of the selected movie
    distances = similarity[movie_index]

    # Get the indices of the most similar movies (excluding the selected movie itself)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []


    for i in movie_list:
        # Correctly access the movie ID using column name 'id'
         # Use column name 'id' instead of 'movie_id'
        movie_id = movies.iloc[i[0]]['movie_id']

        # Append the recommended movie's title and poster
        recommended_movies.append(movies.iloc[i[0]].title)  # Use column name 'title'


    return recommended_movies


# Streamlit interface
st.title('Movie Recommender System')

optionnn= st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    recommendation= recommend(optionnn)
    for i in recommendation:
        st.write(i)


    # Display the recommended movies and their posters

