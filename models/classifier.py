import tensorflow as tf
import joblib

model = tf.keras.models.load_model("price_classifier.keras")
scaler = joblib.load("scaler.pkl")

# Example: predict on new data
# new_scaled = scaler.transform(new_data)
# preds = model.predict(new_scaled).argmax(axis=1)
def predict(new_data):
    new_scaled = scaler.transform(new_data)
    probs = model.predict(new_scaled)
    preds = probs.argmax(axis=1)
    confidence = probs.max(axis=1)
    return preds, confidence