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

- **KISS** — `app.py` is a plain `if/elif` on a CLI arg, no argument-parsing library or extra abstraction for a 2-mode switch.
- **DRY** — `preprocessing.py`'s `prepare_input()` is the single place column ordering + scaling happens, used by both `cli_view.py` and `web_view.py`.
- **YAGNI** — no auth, database, logging, or config system. Just specs in, prediction out.
- **SOLID (SRP/DIP)** — `predict_controller.py` only orchestrates; it calls `predict()` without knowing it's a Keras model under the hood, so swapping models wouldn't require controller changes.
- **SoC** — the `models/` → `controllers/` → `views/` split is the MVC structure itself: each layer is independent and replaceable on its own.
- **Avoid premature optimization** — `classifier.py` calls `model.predict()` directly, no batching/caching/quantization added before there was evidence it was needed.
- **Law of Demeter** — both views call `controller.get_prediction(raw_data)` and get back `{label, confidence}`, never touching `scaler` or `model` directly.
## Design principles applied
- **SoC / MVC** — model, controller, and views don't know about each other's internals.
- **DRY** — `prepare_input()` is the single place raw data becomes model-ready.
- **YAGNI** — no auth, no DB, no logging; just specs in, prediction out.
- **SOLID (SRP/DIP)** — each file has one job; controller depends only on `predict()`'s interface, not its implementation.
- **Law of Demeter** — views call `get_prediction(raw_data)` and never touch `model` or `scaler` directly.
