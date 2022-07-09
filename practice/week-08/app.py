#pip install streamlit_chat
#pip install tensorflow
#pip install konlpy
import streamlit as st
from streamlit_chat import message
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from konlpy.tag import Okt

import pickle
import re
max_len = 30
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
loaded_model = load_model('best_model.h5')


def sentiment_predict(new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    try:
        okt = Okt()
        new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    except Exception as e:
        print(e)
        pass
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    score = float(loaded_model.predict(pad_new)) # 예측
    if(score > 0.5):
        return ("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
    else:
        return ("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))
        
        
st.title("감정분석 앱")

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    

text = st.text_input('Message')
if text:
    message(text, is_user=True)
    with st.spinner():
        message(sentiment_predict(text)) 

