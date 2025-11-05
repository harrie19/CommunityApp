import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np
import os
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 📦 Modell laden
def load_latest_model():
    version = 1
    while os.path.exists(f"model_v{version}.pkl"):
        version += 1
    version -= 1
    with open(f"model_v{version}.pkl", "rb") as f:
        return pickle.load(f), version

model, current_version = load_latest_model()

# 🧱 GUI-Fenster
root = tk.Tk()
root.title("Community KI")

entries = []
for i in range(10):
    tk.Label(root, text=f"Feature {i+1}").grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

result_label = tk.Label(root, text="Vorhersage: ")
result_label.grid(row=10, column=0, columnspan=2)

# 🔮 Vorhersage
def predict():
    try:
        features = [float(e.get()) for e in entries]
        prediction = model.predict([features])[0]
        result_label.config(text=f"Vorhersage: {'Hilfreich' if prediction == 1 else 'Nicht hilfreich'}")
    except:
        messagebox.showerror("Fehler", "Ungültige Eingabe")

# 📊 Feedback speichern
def save_feedback(value):
    try:
        features = [float(e.get()) for e in entries]
        with open("feedback.csv", "a") as f:
            f.write(",".join(map(str, features)) + f",{value}\n")
        messagebox.showinfo("Gespeichert", "Feedback gespeichert")
    except:
        messagebox.showerror("Fehler", "Feedback konnte nicht gespeichert werden")

# 🔁 Retraining starten
def retrain_model():
    if not os.path.exists("feedback.csv"):
        messagebox.showerror("Fehler", "Keine Feedbackdaten vorhanden")
        return

    X, y = [], []
    with open("feedback.csv", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 11:
                X.append([float(x) for x in parts[:10]])
                y.append(int(parts[10]))

    if len(X) < 5:
        messagebox.showwarning("Zu wenig Daten", "Mindestens 5 Feedbacks erforderlich")
        return

    new_model = RandomForestClassifier()
    new_model.fit(X, y)

    # 📦 Modellversionierung
    version = current_version + 1
    model_path = f"model_v{version}.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(new_model, f)

    # 📊 Bewertung
    y_pred = new_model.predict(X[:3])
    metrics = {
        "version": version,
        "accuracy": round(accuracy_score(y[:3], y_pred), 2),
        "precision": round(precision_score(y[:3], y_pred), 2),
        "recall": round(recall_score(y[:3], y_pred), 2),
        "f1_score": round(f1_score(y[:3], y_pred), 2)
    }

    # 📁 Metriken speichern
    if os.path.exists("metrics.json"):
        with open("metrics.json", "r") as f:
            all_metrics = json.load(f)
    else:
        all_metrics = []

    all_metrics.append(metrics)
    with open("metrics.json", "w") as f:
        json.dump(all_metrics, f, indent=2)

    messagebox.showinfo("Retraining abgeschlossen", f"Modell v{version} gespeichert und bewertet")
    global model, current_version
    model = new_model
    current_version = version
    result_label.config(text="Modell aktualisiert")

# 🔘 Buttons
tk.Button(root, text="Vorhersage starten", command=predict).grid(row=11, column=0, columnspan=2)

feedback_frame = tk.Frame(root)
feedback_frame.grid(row=12, column=0, columnspan=2)
tk.Label(feedback_frame, text="Feedback:").pack(side=tk.LEFT)
tk.Button(feedback_frame, text="Hilfreich", command=lambda: save_feedback(1)).pack(side=tk.LEFT)
tk.Button(feedback_frame, text="Nicht hilfreich", command=lambda: save_feedback(0)).pack(side=tk.LEFT)

tk.Button(root, text="Retraining starten", command=retrain_model).grid(row=13, column=0, columnspan=2)

# 🚀 Start
root.mainloop()

