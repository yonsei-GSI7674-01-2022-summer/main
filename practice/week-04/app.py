import mysql.connector
import streamlit as st
from elasticsearch import Elasticsearch

ES_HOST = ""
INDEX_NAME = "movie_index"
es = Elasticsearch(ES_HOST)


HOST = ""
USER = ""
PASSWORD = ""
mydb = mysql.connector.connect(
    host=HOST, user=USER, password=PASSWORD, database="movie_db"
)

st.image("images/logo.png")

query = st.text_input("어떤 영화를 원하시나요?")

if query:
    res = es.search(index=INDEX_NAME, q=query)
    movie_ids = []
    for data in res["hits"]["hits"]:
        movie_ids.append(str(data["_id"]))

    sql = "SELECT * FROM movie WHERE id IN {} ORDER BY FIELD (id, {})".format(
        tuple(movie_ids), ",".join(movie_ids)
    )

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(sql)

    query_result = []
    myresult = mycursor.fetchall()

    for movie in myresult:
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image(movie["image"])
            st.caption(movie["year"])
        with col2:
            st.header(movie["title"])
            st.text(movie["story"])

            st.write(movie["link"])
