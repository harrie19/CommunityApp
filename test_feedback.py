from modules.feedback import FeedbackManager

fb = FeedbackManager()

print(fb.submit_feedback("marek", "predictor", "Vorhersage war hilfreich", rating=5))
print(fb.submit_feedback("lisa", "chat", "Antwort kam zu spät", rating=2))
print(fb.submit_feedback("marek", "auth", "Login war schnell", rating=4))

print("\n📋 Alle Feedbacks:")
for f in fb.get_all_feedback():
    print(f)

print("\n🔍 Feedback zu 'predictor':")
for f in fb.get_feedback_by_module("predictor"):
    print(f)

print("\n👤 Feedback von 'marek':")
for f in fb.get_feedback_by_user("marek"):
    print(f)
