import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


ROOT = "../khana"
OUTPUT_LOCATION = "../paper/figs"

similar_labels = [
    {
        "misal pav": ["0ebc875ab7cc79ee98f4ed2ff88f2b3b","8b440166298df57efbfef3ad01b0eef1","ep2ggyg2cbrevxlkk0sf"], 
        "pav bhaji": ["00dc230428642af31e8e6740588f706f", "5c2d64a36fb5397679e145e41a243060", "ah6d5etgvbd6q7ypitjm"]
    },
    {
        "vada pav": ["yxomcuuxcgvu9h35kutb", "zrvcjqjdg1jq1fcd8gef", "h7kbwwbch6q0fldjdjix"],
        "dabeli": ["2f3550b5dd3f13a8b844987c70a56243", "5ec531121a025dac3c293251670cac1c", "ckgvtqiqwzptn3bxwgqi"]
    }
]

for idx, sim in enumerate(similar_labels):
    images = []
    for label, imgs in sim.items():
        for img in imgs:
            images.append(f"{label}/{img}")
    fig, axs = plt.subplots(2, 3)
    for i, ax in enumerate(axs.flatten()):
        ax.imshow(Image.open(f"{ROOT}/{images[i]}"))
        ax.axis("off")
    plt.tight_layout()
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig(f"{OUTPUT_LOCATION}/similar_items_{idx}.pdf", bbox_inches="tight", pad_inches=0, dpi=150)
    plt.close()
