import streamlit as st
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jungwons/Desktop/Lecture/2022123124/practice/week-06/glassy-life-350815-07dd97f00324.json"
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

if password == "yonsei":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.image(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        text = detect_text(bytes_data)
        st.write(text)
