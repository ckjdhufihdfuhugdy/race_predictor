import streamlit as st
from ocr_module import ocr_image, ocr_pdf
from parse_module import parse_racecard_text
from predict_module import encode_and_predict

st.title("Horse Racing Predictor")

uploaded_file = st.file_uploader(
    "Upload racecard (PDF/image)",
    type=["pdf", "png", "jpg", "jpeg"],
)

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = ocr_pdf(uploaded_file)
    else:
        text = ocr_image(uploaded_file)

    st.subheader("Extracted Text")
    st.text(text[:1000])

    df = parse_racecard_text(text)
    st.subheader("Parsed Racecard")
    st.dataframe(df)

    if not df.empty:
        try:
            result = encode_and_predict(df)
        except FileNotFoundError as e:
            st.error(str(e))
        else:
            st.subheader("Predictions")
            st.dataframe(result)
            st.success(f"Predicted Winner: {result.iloc[0]['horse']}")
