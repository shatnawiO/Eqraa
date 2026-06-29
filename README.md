# Mobile Price Classifier

Predicts a phone's price range (Low / Medium / High / Very high) from its specs,
using a neural network trained on the Kaggle Mobile Price Classification dataset.

## Run
- CLI: `python app.py cli`
- Web: `python app.py web`

## Structure
emotion_classifier/

├── models/

│   ├── classifier.py       # loads model, runs prediction only

│   └── preprocessing.py    # feature order + scaling, shared by training & inference

├── controllers/

│   └── predict_controller.py   # orchestrates: preprocess -> predict -> label

├── views/

│   ├── cli_view.py          # terminal input/output

│   └── web_view.py          # Flask form input/output

└── app.py                   # entry point
## Design principles applied
- **SoC / MVC** — model, controller, and views don't know about each other's internals.
- **DRY** — `prepare_input()` is the single place raw data becomes model-ready.
- **YAGNI** — no auth, no DB, no logging; just specs in, prediction out.
- **SOLID (SRP/DIP)** — each file has one job; controller depends only on `predict()`'s interface, not its implementation.
- **Law of Demeter** — views call `get_prediction(raw_data)` and never touch `model` or `scaler` directly.