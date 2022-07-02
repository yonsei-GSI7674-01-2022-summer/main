import streamlit as st
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "json파일의 GCP 서버상의 절대 경로를 넣어주세요!"
st.title("Yonsei AI")

password = st.text_input("password")

def detect_text(content):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()


    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    return texts[0].description

def gen_audio(text):
    #TODO
     with open("output.wav", "wb") as out:
        out.write(bytes("randomTHING", 'utf-8'))
def transcribe_file(speech_file):
    #TODO
    return "Hello"


if password == "yonsei":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.image(uploaded_file)
        
        st.header("Image-to-Text")
        bytes_data = uploaded_file.getvalue()
        text = detect_text(bytes_data)
        st.write(text)
        
        st.header("Text-to-Audio")
        gen_audio(text)
        audio_file = open('output.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        
        st.header("Audio-to-Text")
        text = transcribe_file("output.wav")
        st.write(text)
