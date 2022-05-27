import streamlit as st
import matplotlib.pyplot as plt
import cv2
import numpy as np
# 캐스케이드 파일 지정해서 검출기 생성하기 --- (*1)
cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)




st.title("Mosaic App")
st.subheader("초상권이 걱정되시나요? 한번에 모자이크 처리를 해주세요!")


my_pic = st.file_uploader("사진을 올려주세요!")
if my_pic:
    #TODO
    bytes_data = my_pic.getvalue()
    img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    face_list = cascade.detectMultiScale(img_gray)
    if len(face_list) == 0: 
        st.write("얼굴인식 실패")
    else:
        for (x,y,w,h) in face_list:
            red = (0, 0, 255)
            cv2.rectangle(img, (x, y), (x+w, y+h), red, thickness=10)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(img, caption="와우!")
