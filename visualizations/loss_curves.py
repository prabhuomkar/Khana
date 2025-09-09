import os
import csv
import matplotlib.pyplot as plt


OUTPUT_LOCATION = "../paper/figs"

data = {}

for model in os.listdir("metrics"):
    data[model.replace(".csv", "")] = []
    with open(f"metrics/{model}", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[model.replace(".csv", "")].append(row)
            if row["Epoch"] == "50":
                break

for idx, (model, curve_points) in enumerate(data.items()):
    epochs = [int(point["Epoch"]) for point in curve_points]
    train_losses = [float(point["Train Loss"]) for point in curve_points]

    plt.figure(figsize=(16, 8))
    plt.rcParams["font.family"] = "Fira Code"

    ax = plt.gca()
    ax.tick_params(axis="both", which="both", length=0, labelsize=24)
    ax.tick_params(axis="both", which="both", width=0, labelsize=24)
    ax.grid(axis="both", linestyle="--", linewidth=1)
    plt.plot(epochs, train_losses, "-o", label="Train Loss", color="#F8474A", linewidth=2)
    plt.xlabel("Epoch", fontsize=24)
    plt.legend(fontsize=24)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_LOCATION}/loss_curves_{idx}_{model}.pdf", pad_inches=0, dpi=150)
    plt.close()
