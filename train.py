import torch
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

# 💾 Beste Konfiguration speichern
BEST_CONFIG = {"lr": 0.0005, "dropout": 0.4, "batch_size": 32}

# 🔢 Daten laden und vorbereiten
def prepare_data(path="data.csv"):
    df = pd.read_csv(path)
    df = df.dropna(subset=["target"])
    df["target"] = df["target"].astype(int)

    X = df.drop("target", axis=1).values
    y = df["target"].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    joblib.dump(scaler, "scaler.pkl")  # 📦 Scaler speichern

    return train_test_split(X, y, test_size=0.3, random_state=42)

# 🧠 Modell A
def build_model():
    return torch.nn.Sequential(
        torch.nn.Linear(10, 64),
        torch.nn.ReLU(),
        torch.nn.Dropout(0.3),
        torch.nn.Linear(64, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, 2)
    )

# 🧠 Modell B (Variante)
def build_model_variant():
    return torch.nn.Sequential(
        torch.nn.Linear(10, 128),
        torch.nn.ReLU(),
        torch.nn.Dropout(0.4),
        torch.nn.Linear(128, 64),
        torch.nn.ReLU(),
        torch.nn.Linear(64, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, 2)
    )

# 🧠 Bestes Modell aus Konfiguration
def build_best_model():
    return torch.nn.Sequential(
        torch.nn.Linear(10, 64),
        torch.nn.ReLU(),
        torch.nn.Dropout(BEST_CONFIG["dropout"]),
        torch.nn.Linear(64, 32),
        torch.nn.ReLU(),
        torch.nn.Linear(32, 2)
    )

# 🏋️‍♂️ Training
def train_model(model, loader, lr=0.001):
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    for epoch in range(10):
        for batch_x, batch_y in loader:
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 📊 Evaluation
def evaluate_model(model, loader, name="Modell"):
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for batch_x, batch_y in loader:
            outputs = model(batch_x)
            _, predicted = torch.max(outputs, 1)
            all_preds.extend(predicted.numpy())
            all_labels.extend(batch_y.numpy())
    acc = accuracy_score(all_labels, all_preds)
    cm = confusion_matrix(all_labels, all_preds)
    print(f"\n📊 Evaluation {name}")
    print(f"Gesamt-Accuracy: {acc:.2f}")
    print("Confusion Matrix:")
    print(cm)

# 🔁 Hyperparameter-Experimente
def run_experiments(configs, X_train, y_train, X_test, y_test):
    for i, cfg in enumerate(configs):
        print(f"\n🔧 Experiment {i+1}: lr={cfg['lr']}, dropout={cfg['dropout']}, batch={cfg['batch_size']}")

        model = torch.nn.Sequential(
            torch.nn.Linear(10, 64),
            torch.nn.ReLU(),
            torch.nn.Dropout(cfg['dropout']),
            torch.nn.Linear(64, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 2)
        )

        train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32),
                                      torch.tensor(y_train, dtype=torch.long))
        test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32),
                                     torch.tensor(y_test, dtype=torch.long))

        train_loader = DataLoader(train_dataset, batch_size=cfg['batch_size'], shuffle=True)
        test_loader = DataLoader(test_dataset, batch_size=cfg['batch_size'], shuffle=False)

        train_model(model, train_loader, lr=cfg['lr'])
        evaluate_model(model, test_loader, name=f"Experiment {i+1}")

# 🚀 Hauptablauf
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_data()

    # 🔁 Hyperparameter-Vergleich
    configs = [
        {"lr": 0.001, "dropout": 0.3, "batch_size": 16},
        {"lr": 0.0005, "dropout": 0.4, "batch_size": 32},
        {"lr": 0.0001, "dropout": 0.2, "batch_size": 64}
    ]
    run_experiments(configs, X_train, y_train, X_test, y_test)

    # 🧠 Bestes Modell trainieren und speichern
    train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32),
                                  torch.tensor(y_train, dtype=torch.long))
    test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32),
                                 torch.tensor(y_test, dtype=torch.long))

    best_train_loader = DataLoader(train_dataset, batch_size=BEST_CONFIG["batch_size"], shuffle=True)
    best_test_loader = DataLoader(test_dataset, batch_size=BEST_CONFIG["batch_size"], shuffle=False)

    model_best = build_best_model()
    train_model(model_best, best_train_loader, lr=BEST_CONFIG["lr"])
    torch.save(model_best.state_dict(), "model_best.pt")
    evaluate_model(model_best, best_test_loader, name="Bestes Modell")

