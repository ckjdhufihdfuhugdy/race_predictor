# predict_module.py
import joblib
import numpy as np

# Load encoders and model once at startup
race_model = joblib.load('models/race_model.joblib')
le_jockey = joblib.load('models/le_jockey.joblib')
le_trainer = joblib.load('models/le_trainer.joblib')
# ...etc

def encode_and_predict(df):
    # Encode as your model expects
    df['jockey_enc'] = le_jockey.transform(df['jockey'].fillna('Unknown'))
    df['trainer_enc'] = le_trainer.transform(df['trainer'].fillna('Unknown'))
    # ...repeat for all categorical features

    features = df[['jockey_enc', 'trainer_enc', ...]]  # Fill in all model features here
    preds = race_model.predict_proba(features)[:,1]    # Or however your model outputs probability
    df['win_probability'] = preds
    return df.sort_values('win_probability', ascending=False)
