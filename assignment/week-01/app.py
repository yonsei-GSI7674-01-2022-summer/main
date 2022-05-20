import streamlit as st
st.title("Hello")
my_name = st.text_input("이름이 어떻게 되시나요?")
if my_name:
    st.text('안녕하세요 {}님!'.format(my_name))

my_pic = st.file_uploader("사진을 올려주세요!")
if my_pic:
    st.image(my_pic, "멋지네요 {}님".format(my_name))
