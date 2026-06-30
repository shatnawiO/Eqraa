import tensorflow as tf
import joblib

model = tf.keras.models.load_model("price_classifier.keras")
scaler = joblib.load("scaler.pkl")


def predict(new_data):
    probs = model.predict(new_data)
    preds = probs.argmax(axis=1)
    confidence = probs.max(axis=1)
    return preds, confidence