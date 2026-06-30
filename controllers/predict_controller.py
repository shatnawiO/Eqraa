from models.classifier import predict , scaler
from models.preprocessing import prepare_input


PRICE_LABELS = {0: "Low cost", 1: "Medium cost", 2: "High cost", 3: "Very high cost"}

def get_prediction(raw_data):
    scaled = prepare_input(raw_data, scaler)
    preds, confidence = predict(scaled)

    return {
        "label": PRICE_LABELS[int(preds[0])],
        "confidence": round(float(confidence[0]), 4)
    }