import streamlit as st
import easyocr
from PIL import Image
import numpy as np

def extract_text(image_path, lang='en'):
    reader = easyocr.Reader([lang])
    results = reader.readtext(np.array(image_path))
    
    all_text = ''
    confidences = []

    for (bbox, text, prob) in results:
        all_text += ' ' + text
        confidences.append(prob)

    final_confidence = sum(confidences) / len(confidences) if confidences else 0
    return all_text, final_confidence

st.title(' Text from Image')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Hold tight..")
    extracted_text, confidence = extract_text(image, 'en')
    st.write("Extracted Text")
    st.text_area("Result", extracted_text, height=150)
    st.write(f"Confidence: {confidence*100:.2f}%")
