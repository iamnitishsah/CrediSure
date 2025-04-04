import pandas as pd
import tensorflow as tf
import joblib
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'lender', 'neural_network_model.keras')
PREPROCESSOR_PATH = os.path.join(settings.BASE_DIR, 'lender', 'model_info.pkl')

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    model_info = joblib.load(PREPROCESSOR_PATH)
    preprocessor = model_info['preprocessor']
    categorical_cols = model_info['categorical_cols']
    numerical_cols = model_info['numerical_cols']
except FileNotFoundError as e:
    raise Exception(f"Model or preprocessor file not found: {e}")

def predict_risk(data):
    required_cols = numerical_cols + categorical_cols
    input_data = {col: [data.get(col, 0) if col in numerical_cols else data.get(col, '')] for col in required_cols}
    new_data = pd.DataFrame(input_data)

    processed_data = preprocessor.transform(new_data)

    default_prob = model.predict(processed_data, verbose=0)[0][0]

    credit_score = int(100 - default_prob * 100)

    if credit_score >= 80:
        risk_level = "Very Low Risk"
    elif credit_score >= 60:
        risk_level = "Low Risk"
    elif credit_score >= 40:
        risk_level = "Moderate Risk"
    elif credit_score >= 20:
        risk_level = "High Risk"
    else:
        risk_level = "Very High Risk"

    return {
        'credit_score': credit_score,
        'risk_level': risk_level
    }