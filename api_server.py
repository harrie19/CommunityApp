from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import pickle
import os
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

app = FastAPI()

# 🔐 Token-Schutz
API_TOKEN = "community-secret-2025"

# 📦 Modell laden
def load_latest_model():
    version = 1
    while os.path.exists(f"model_v{version}.pkl"):
        version += 1
    version -= 1
    with open(f"model_v{version}.pkl", "rb") as f:
        return pickle.load(f), version

model, current_version = load_latest_model()

# 📥 Datenmodelle
class FeatureInput(BaseModel):
    features: list[float]

class FeedbackInput(BaseModel):
    features: list[float]
    label: int

# 🔮 Vorhersage
@app.post("/predict")
def predict(data: FeatureInput, token: str = Header(...)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Ungültiger Token")
    prediction = model.predict([data.features])[0]
    return {"prediction": int(prediction)}

# 📊 Feedback speichern
@app.post("/feedback")
def save_feedback(data: FeedbackInput, token: str = Header(...)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Ungültiger Token")
    with open("feedback.csv", "a") as f:
        f.write(",".join(map(str, data.features)) + f",{data.label}\n")
    return {"status": "Feedback gespeichert"}

# 🔁 Retraining
@app.post("/retrain")
def retrain(token: str = Header(...)):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Ungültiger Token")

    if not os.path.exists("feedback.csv"):
        return {"error": "Keine Feedbackdaten vorhanden"}

    X, y = [], []
    with open("feedback.csv", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 11:
                X.append([float(x) for x in parts[:10]])
                y.append(int(parts[10]))

    if len(X) < 5:
        return {"error": "Mindestens 5 Feedbacks erforderlich"}

    new_model = RandomForestClassifier()
    new_model.fit(X, y)

    version = current_version + 1
    model_path = f"model_v{version}.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(new_model, f)

    y_pred = new_model.predict(X[:3])
    metrics = {
        "version": version,
        "accuracy": round(accuracy_score(y[:3], y_pred), 2),
        "precision": round(precision_score(y[:3], y_pred), 2),
        "recall": round(recall_score(y[:3], y_pred), 2),
        "f1_score": round(f1_score(y[:3], y_pred), 2)
    }

    if os.path.exists("metrics.json"):
        with open("metrics.json", "r") as f:
            all_metrics = json.load(f)
    else:
        all_metrics = []

    all_metrics.append(metrics)
    with open("metrics.json", "w") as f:
        json.dump(all_metrics, f, indent=2)

    return {"status": f"Modell v{version} trainiert", "metrics": metrics}
