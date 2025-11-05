import json
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.metrics import confusion_matrix

# 📦 Metriken laden
with open("metrics.json", "r") as f:
    metrics = json.load(f)

# 📊 Metriken plotten
versions = [m["version"] for m in metrics]
accuracy = [m["accuracy"] for m in metrics]
precision = [m["precision"] for m in metrics]
recall = [m["recall"] for m in metrics]
f1 = [m["f1_score"] for m in metrics]

plt.figure(figsize=(10, 6))
plt.plot(versions, accuracy, label="Accuracy")
plt.plot(versions, precision, label="Precision")
plt.plot(versions, recall, label="Recall")
plt.plot(versions, f1, label="F1-Score")
plt.xlabel("Version")
plt.ylabel("Score")
plt.title("Modellmetriken über Versionen")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("metrics_trend.png")
plt.close()

# 🧠 Confusion Matrix pro Modell
for m in metrics:
    version = m["version"]
    model_path = f"model_v{version}.pkl"
    if not pickle or not model_path:
        continue
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Dummy-Daten für Vergleich
    X = [[0.1 * i for i in range(1, 11)],
         [0.2 * i for i in range(1, 11)],
         [0.3 * i for i in range(1, 11)]]
    y_true = [0, 1, 1]
    y_pred = model.predict(X)

    cm = confusion_matrix(y_true, y_pred)
    plt.figure()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Confusion Matrix v{version}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(f"confusion_v{version}.png")
    plt.close()

print("✅ Vergleich abgeschlossen: metrics_trend.png + confusion_vX.png")
