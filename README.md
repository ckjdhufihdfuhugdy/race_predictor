# Horse Racing Predictor

This app lets you upload a racecard as a PDF or image and predicts the likely winner.

## Setup

1. Install Python 3.8 or newer.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the trained model `race_model.joblib` and the label encoder files (`le_course.joblib`, `le_going.joblib`, `le_jockey.joblib`, `le_trainer.joblib`, `le_type.joblib`) in the project directory.

## Running

Launch the Streamlit app from the project root:

```bash
streamlit run app.py
```

Upload a PDF or image of a racecard. If the text matches the parser, predictions will be displayed and the top horse will be shown as the predicted winner.
