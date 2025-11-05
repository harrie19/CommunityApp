import os
import pickle
from sklearn.ensemble import RandomForestClassifier

class CommunityPredictor:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        if os.path.exists("model.pkl"):
            with open("model.pkl", "rb") as f:
                print("📦 Modell geladen aus model.pkl")
                return pickle.load(f)
        else:
            print("⚠️ Kein trainiertes Modell gefunden – nutze Default-Modell")
            return RandomForestClassifier().fit([[0]*10], [0])  # Dummy-Modell

    def predict(self, features):
        return self.model.predict([features])[0]
