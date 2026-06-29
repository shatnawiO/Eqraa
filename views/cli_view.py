from controllers.predict_controller import get_prediction
from models.preprocces import FEATURE_COLUMNS

def run():
    print("Enter phone specs:")
    raw_data = {}
    for col in FEATURE_COLUMNS:
        value = float(input(f"{col}: "))
        raw_data[col] = [value]  # wrap in list so it forms a 1-row table

    result = get_prediction(raw_data)
    print(f"\nPredicted price range: {result['label']} (confidence: {result['confidence']})")

if __name__ == "__main__":
    run()