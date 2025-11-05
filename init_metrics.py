import json
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 📦 Dummy-Daten
X = [
    [0.5, 1.2, -0.3, 0.8, 1.1, -0.7, 0.0, 0.4, -1.2, 0.6],
    [1.0, -0.5, 0.3, 0.9, -1.1, 0.2, 0.1, -0.4, 1.2, -0.6],
    [-0.2, 0.7, 1.3, -0.8, 0.5, 0.0, -1.0, 0.6, 0.9, -0.3]
]
y = [1, 0, 0]

# 🧠 Modell trainieren
model = RandomForestClassifier()
model.fit(X, y)

# 💾 Modell speichern
with open("model_v1.pkl", "wb") as f:
    pickle.dump(model, f)

# 📊 Metriken berechnen
y_pred = model.predict(X)
metrics = {
    "version": 1,
    "accuracy": round(accuracy_score(y, y_pred), 2),
    "precision": round(precision_score(y, y_pred), 2),
    "recall": round(recall_score(y, y_pred), 2),
    "f1_score": round(f1_score(y, y_pred), 2)
}

# 📁 Metriken speichern
with open("metrics.json", "w") as f:
    json.dump([metrics], f, indent=2)

print("✅ metrics.json initialisiert und model_v1.pkl erzeugt")
