# app.py
import streamlit as st
from ocr_module import ocr_image, ocr_pdf
from parse_module import parse_racecard_text
from predict_module import encode_and_predict

st.title("Horse Racing Predictor")

uploaded_file = st.file_uploader("Upload racecard (PDF/image)", type=['pdf', 'png', 'jpg', 'jpeg'])

if uploaded_file:
    if uploaded_file.type == 'application/pdf':
        text = ocr_pdf(uploaded_file)
    else:
        text = ocr_image(uploaded_file)
    
    st.subheader("Extracted Text")
    st.text(text[:1000])  # Preview first 1000 chars

    df = parse_racecard_text(text)
    st.subheader("Parsed Racecard")
    st.dataframe(df)

    if not df.empty:
        result = encode_and_predict(df)
        st.subheader("Predictions")
        st.dataframe(result)
        st.success(f"Predicted Winner: {result.iloc[0]['horse']}")

        # Add: star ratings, tips, etc. here!
