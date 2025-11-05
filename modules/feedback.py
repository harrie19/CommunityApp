from datetime import datetime

class FeedbackManager:
    def __init__(self):
        self.feedback_log = []  # Liste von Feedback-Einträgen

    def submit_feedback(self, username, module, message, rating=None, features=None):
        entry = {
            "user": username,
            "module": module,
            "message": message,
            "rating": rating,
            "features": features,
            "timestamp": datetime.now().isoformat()
        }
        self.feedback_log.append(entry)
        return "✅ Feedback gespeichert"

    def get_all_feedback(self):
        return self.feedback_log

    def get_feedback_by_module(self, module):
        return [f for f in self.feedback_log if f["module"] == module]

    def get_feedback_by_user(self, username):
        return [f for f in self.feedback_log if f["user"] == username]

    def export_feedback_for_training(self):
        training_data = []
        for entry in self.feedback_log:
            label = 1 if entry.get("rating", 0) >= 4 else 0
            features = entry.get("features", None)
            if features and isinstance(features, list) and len(features) == 10:
                training_data.append((features, label))
        return training_data
