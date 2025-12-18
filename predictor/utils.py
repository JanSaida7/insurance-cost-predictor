import joblib
import os
from django.conf import settings

def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'model_linear_reg.pkl')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = joblib.load(model_path)
    return model
