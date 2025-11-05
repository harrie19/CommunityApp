from modules.loop import KILoop
from sklearn.ensemble import RandomForestClassifier
import pickle

# 🔄 Feedback holen
loop = KILoop()
data = loop.feedback.export_feedback_for_training()

# 📊 Features und Labels trennen
X = [features for features, label in data]
y = [label for features, label in data]

print(f"📦 Trainingsdatensätze gefunden: {len(X)}")

# 🔁 Automatisches Training ab 50 Datensätzen
if len(X) < 50:
    print("⏳ Noch nicht genug neue Daten für Retraining")
    exit()

# 🧠 Modell trainieren
model = RandomForestClassifier()
model.fit(X, y)

# 💾 Modell speichern
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modell wurde automatisch neu trainiert und gespeichert")
