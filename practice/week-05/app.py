import streamlit as st
import pandas as pd
import numpy as np
st.image("logo.png")


movie_title = st.text_input("어떤 영화와 비슷한 영화를 찾으시나요?")
with st.spinner():
    movies = pd.read_csv("movies.csv",sep="\t")
    indices = pd.read_csv("index.csv", header = None, index_col = 0, squeeze = True)
    with open('sim.npy', 'rb') as f:
        cosine_sim = np.load(f)
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx_list = list(indices.keys().str.replace(" ", "")[1:])
        idx, movie_title = [(idx, s) for idx, s in enumerate(idx_list) if title in s][0]
        st.write(movie_title,"와 비슷한 영화는:")

    except Exception as e:
        print(e)
        print("해당 영화가 존재하지 않습니다.")
        return []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movie_indices



if movie_title:
    movies_indices = get_recommendations(movie_title)

    for movie in movies.iloc[movies_indices].to_dict(orient='records'):
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image(movie["poster"])
            st.caption(movie["year"])
        with col2:
            st.header(movie["title"])
            st.text(movie["story"])

            st.write(movie["url"])
