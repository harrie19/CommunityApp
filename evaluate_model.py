import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# 📦 Modell laden
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ Modell erfolgreich geladen")
except FileNotFoundError:
    print("❌ model.pkl nicht gefunden")
    exit()

# 🧪 Testdaten (z. B. aus Feedback oder manuell)
X_test = [
    [0.5, 1.2, -0.3, 0.8, 1.1, -0.7, 0.0, 0.4, -1.2, 0.6],
    [1.0, -0.5, 0.3, 0.9, -1.1, 0.2, 0.1, -0.4, 1.2, -0.6],
    [-0.2, 0.7, 1.3, -0.8, 0.5, 0.0, -1.0, 0.6, 0.9, -0.3]
]
y_true = [1, 0, 0]

# 🔮 Vorhersagen
y_pred = model.predict(X_test)

# 📊 Metriken berechnen
print("\n📊 Bewertungsmetriken:")
print(f"Accuracy:  {accuracy_score(y_true, y_pred):.2f}")
print(f"Precision: {precision_score(y_true, y_pred):.2f}")
print(f"Recall:    {recall_score(y_true, y_pred):.2f}")
print(f"F1-Score:  {f1_score(y_true, y_pred):.2f}")

# 📉 Confusion Matrix anzeigen
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(4, 3))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Nicht hilfreich", "Hilfreich"],
            yticklabels=["Nicht hilfreich", "Hilfreich"])
plt.xlabel("Vorhergesagt")
plt.ylabel("Tatsächlich")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

