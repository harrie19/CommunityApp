import zipfile
import os

# 📁 Dateien definieren
files_to_export = []
if os.path.exists("feedback.csv"):
    files_to_export.append("feedback.csv")
if os.path.exists("metrics.json"):
    files_to_export.append("metrics.json")

# 📦 Alle Modellversionen hinzufügen
for file in os.listdir():
    if file.startswith("model_v") and file.endswith(".pkl"):
        files_to_export.append(file)

# 📦 ZIP erstellen
with zipfile.ZipFile("community_export.zip", "w") as zipf:
    for file in files_to_export:
        zipf.write(file)

print("✅ Export abgeschlossen: community_export.zip")
