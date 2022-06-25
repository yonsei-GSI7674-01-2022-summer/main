import streamlit as st
import os
from google.cloud import storage
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jungwons/Dropbox/Lecture/2022-summer/ibk/main/practice/week-06/glassy-life-350815-e5dc707dd5b3.json"



storage_client = storage.Client()
bucket_name = "my-yonsei-bucket-2022123124"
st.title("Data Collector")


gender = st.selectbox('Gender',('Female','Male'))
age = st.number_input('Age',value=33)
mask = st.checkbox('Mask')
# picture = st.camera_input("Take a picture")
picture = st.file_uploader("Choose a file")
if picture:
    st.image(picture)
    st.write(gender,age,mask, time.time())
    file_name = "-".join([gender,str(age),str(mask), str(time.time())])
    bytes_data = picture.read()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(bytes_data)



