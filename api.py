import torch
import numpy as np
import joblib
import logging
from flask import Flask, request, jsonify

# 🧠 Modellstruktur
def build_best_model():
    return torch.nn.Sequential(
        torch.nn.Linear(10, 64),
        torch.nn.ReLU(),
        torch.nn.Dropout(0.4),
        torch.nn.Linear(64, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, 2)
    )

# 🔧 Logging konfigurieren
logging.basicConfig(level=logging.INFO)

# 📦 Modell & Scaler laden mit Fehlerbehandlung
try:
    model = build_best_model()
    model.load_state_dict(torch.load("model_best.pt"))
    model.eval()
    logging.info("✅ Modell geladen")
except Exception as e:
    logging.error(f"❌ Modell konnte nicht geladen werden: {e}")
    model = None

try:
    scaler = joblib.load("scaler.pkl")
    logging.info("✅ Scaler geladen")
except Exception as e:
    logging.error(f"❌ Scaler konnte nicht geladen werden: {e}")
    scaler = None

# 🚀 Flask-App starten
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or scaler is None:
        return jsonify({"error": "Modell oder Scaler nicht verfügbar"}), 500

    data = request.get_json()
    logging.info(f"📥 Anfrage erhalten: {data}")

    if not data or "features" not in data:
        return jsonify({"error": "Bitte sende JSON mit 'features': [10 Werte]"}), 400

    try:
        X = np.array([data["features"]])
        if X.shape[1] != 10:
            return jsonify({"error": "Genau 10 Features erforderlich"}), 400

        X_scaled = scaler.transform(X)
        X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

        with torch.no_grad():
            output = model(X_tensor)
            _, prediction = torch.max(output, 1)

        logging.info(f"📤 Vorhersage: {prediction.item()}")
        return jsonify({"prediction": int(prediction.item())})
    except Exception as e:
        logging.error(f"❌ Fehler bei Vorhersage: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
