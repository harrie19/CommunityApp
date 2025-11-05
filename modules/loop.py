from core.predictor import CommunityPredictor
from modules.feedback import FeedbackManager

class KILoop:
    def __init__(self):
        self.predictor = CommunityPredictor()
        self.feedback = FeedbackManager()

    def run_prediction_and_collect_feedback(self, username, features):
        prediction = self.predictor.predict(features)
        print(f"🔮 Vorhersage für {username}: {prediction}")

        message = "Vorhersage war hilfreich" if prediction == 1 else "Vorhersage war unklar"
        rating = 5 if prediction == 1 else 2

        self.feedback.submit_feedback(username, "predictor", message, rating, features=features)
        print(f"📊 Feedback gespeichert: {message} ({rating}/5)")

    def analyze_feedback(self):
        all_fb = self.feedback.get_feedback_by_module("predictor")
        positives = [f for f in all_fb if f["rating"] >= 4]
        negatives = [f for f in all_fb if f["rating"] <= 2]
        print(f"✅ Positive Rückmeldungen: {len(positives)}")
        print(f"❌ Negative Rückmeldungen: {len(negatives)}")
