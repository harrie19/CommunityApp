import json
import matplotlib.pyplot as plt

# 📁 Metriken laden
with open("metrics.json", "r") as f:
    metrics = json.load(f)

# 📊 Daten extrahieren
versions = [m["version"] for m in metrics]
accuracy = [m["accuracy"] for m in metrics]
precision = [m["precision"] for m in metrics]
recall = [m["recall"] for m in metrics]
f1 = [m["f1_score"] for m in metrics]

# 📈 Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(versions, accuracy, label="Accuracy", marker="o")
plt.plot(versions, precision, label="Precision", marker="o")
plt.plot(versions, recall, label="Recall", marker="o")
plt.plot(versions, f1, label="F1-Score", marker="o")

plt.title("Modellmetriken über Versionen")
plt.xlabel("Modellversion")
plt.ylabel("Wert")
plt.ylim(0, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
