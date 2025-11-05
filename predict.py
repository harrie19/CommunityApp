import torch
import numpy as np
import joblib  # Scaler laden
from sklearn.preprocessing import StandardScaler

# 🧠 Beste Modellstruktur
def build_best_model():
    return torch.nn.Sequential(
        torch.nn.Linear(10, 64),
        torch.nn.ReLU(),
        torch.nn.Dropout(0.4),
        torch.nn.Linear(64, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, 2)
    )

# 📦 Modell laden
model = build_best_model()
model.load_state_dict(torch.load("model_best.pt"))
model.eval()

# 📦 Scaler laden
scaler = joblib.load("scaler.pkl")

# 🔢 Neue Eingabedaten (Beispiel mit 10 Features)
X_new = np.array([[0.5, 1.2, -0.3, 0.8, 1.1, -0.7, 0.0, 0.4, -1.2, 0.6]])

# 🔁 Skalieren wie im Training
X_new_scaled = scaler.transform(X_new)

# 🔁 In Tensor umwandeln
X_tensor = torch.tensor(X_new_scaled, dtype=torch.float32)

# 🧠 Vorhersage
with torch.no_grad():
    output = model(X_tensor)
    _, prediction = torch.max(output, 1)
    print("📊 Vorhergesagte Klasse:", prediction.item())

