import tensorflow as tf
import joblib

model = tf.keras.models.load_model("C:\\Users\\USER\\Desktop\\Eqraa\\models\\price_classifier.keras")
scaler = joblib.load("C:\\Users\\USER\\Desktop\\Eqraa\\models\\scaler.pkl")


def predict(new_data):
    probs = model.predict(new_data)
    preds = probs.argmax(axis=1)
    confidence = probs.max(axis=1)
    return preds, confidence