from modules.loop import KILoop
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
import os
import json

# 🔄 KI-Schleife starten
loop = KILoop()

# 📥 Beispiel-Features für 5 Nutzer
features_list = [
    [0.5, 1.2, -0.3, 0.8, 1.1, -0.7, 0.0, 0.4, -1.2, 0.6],
    [1.0, -0.5, 0.3, 0.9, -1.1, 0.2, 0.1, -0.4, 1.2, -0.6],
    [-0.2, 0.7, 1.3, -0.8, 0.5, 0.0, -1.0, 0.6, 0.9, -0.3],
    [0.4, -1.2, 0.8, 1.0, -0.5, 0.3, 0.2, -0.7, 1.1, 0.0],
    [0.9, 0.1, -0.6, 0.7, -1.3, 0.4, 0.5, -0.2, 1.0, -0.9]
]

# 📊 Vorhersagen + Feedback sammeln
for i, features in enumerate(features_list):
    username = f"user{i}"
    loop.run_prediction_and_collect_feedback(username, features)

# 📈 Feedback-Analyse anzeigen
loop.analyze_feedback()

# 📦 Trainingsdaten exportieren
data = loop.feedback.export_feedback_for_training()

print("\n📦 Trainingsdaten:")
for features, label in data:
    print(f"Features: {features} → Label: {label}")

# 🔁 Retraining nur bei genug Feedback
if len(data) < 5:
    print("⏳ Noch nicht genug Feedback für Retraining")
    exit()

# 🧠 Modell trainieren
X = [features for features, label in data]
y = [label for features, label in data]

model = RandomForestClassifier()
model.fit(X, y)

# 💾 Modellversion bestimmen
version = 1
while os.path.exists(f"model_v{version}.pkl"):
    version += 1

# 💾 Modell speichern
model_path = f"model_v{version}.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Modell erfolgreich trainiert und gespeichert als {model_path}")

# 📊 Bewertung nach Training
X_test = X[:3]
y_true = y[:3]
y_pred = model.predict(X_test)

metrics = {
    "version": version,
    "accuracy": round(accuracy_score(y_true, y_pred), 2),
    "precision": round(precision_score(y_true, y_pred), 2),
    "recall": round(recall_score(y_true, y_pred), 2),
    "f1_score": round(f1_score(y_true, y_pred), 2)
}

print("\n📊 Bewertung nach Training:")
for k, v in metrics.items():
    if k != "version":
        print(f"{k.capitalize()}: {v:.2f}")

# 📁 Metriken speichern
metrics_file = "metrics.json"
if os.path.exists(metrics_file):
    with open(metrics_file, "r") as f:
        all_metrics = json.load(f)
else:
    all_metrics = []

all_metrics.append(metrics)

with open(metrics_file, "w") as f:
    json.dump(all_metrics, f, indent=2)

print(f"📁 Metriken gespeichert in {metrics_file}")
