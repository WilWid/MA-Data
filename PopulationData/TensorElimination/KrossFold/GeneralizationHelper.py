import os
import re
import numpy as np

# Ordner mit den Textdateien (aktueller Ordner)
FOLDER = "."

# Regex für Loss-Zeilen
LOSS_PATTERN = re.compile(r"^Loss:\s*([0-9.eE+-]+)")

for filename in os.listdir(FOLDER):
    if not filename.endswith(".txt"):
        continue

    filepath = os.path.join(FOLDER, filename)

    with open(filepath, "r") as f:
        lines = f.readlines()

    losses = []

    # Loss-Werte extrahieren
    for line in lines:
        match = LOSS_PATTERN.match(line.strip())
        if match:
            losses.append(float(match.group(1)))

    if len(losses) != 10:
        print(f"⚠️  {filename}: Erwartet 10 Loss-Werte, gefunden {len(losses)}")
        continue

    mean_loss = np.mean(losses)
    std_loss = np.std(losses, ddof=0)  # Population-Std, wie meist üblich

    # Letzte zwei Zeilen ersetzen
    new_lines = lines[:-2]
    new_lines.append(f"Average GEP Loss: {mean_loss:.6e}\n")
    new_lines.append(f"Standard Deviation of Loss: {std_loss:.6e}\n")

    # Datei überschreiben
    with open(filepath, "w") as f:
        f.writelines(new_lines)

    print(f"✅ {filename} aktualisiert")
