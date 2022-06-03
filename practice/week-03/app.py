import streamlit as st
import mysql.connector
HOST = "DB아이피주소"
USER = "root"
PASSWORD = "비밀번호"
mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  password=PASSWORD,
  database="mydb"
)
st.image("images/logo.png")

keyword = st.text_input("검색어 입력")

if keyword:
    sql = "SELECT * FROM posts WHERE content LIKE '%{}%'".format(keyword)

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(sql)


    posts = mycursor.fetchall()
    #TODO
    for post in range(30):
        st.header('title')

        st.text('content')
        col1, col2 = st.columns([1,5])
        with col1:
            st.caption('createdAt')
        with col2:
            st.write('link')