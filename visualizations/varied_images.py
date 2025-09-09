import os
import matplotlib.pyplot as plt
from PIL import Image

ROOT = "../khana"
OUTPUT_LOCATION = "../paper/figs"

labels = {
    "masala dosa": ["0a0e551b378c42f97b6c987dcb040708", "0ccafa6e3932a5b19fd1084c8ff4f86e", "1ef61c614989aa8a9e2fa76770a43782", "23b325e614428aa02c575c101e73f7d0"], 
    "sev puri": ["0b0d2b0ecb14e38512d29c93f4381f60", "02b16c4136cb392f32fa13cb4a4e57f6", "9bd2d6b7f3e7ddd3c3533991114c25a2", "rorkfpeabtgzbaoehu1j"], 
    "rasgulla": ["000b19e1449b4c876983987887bbc0f8", "1d2ba7d8d1b56bea93da94fda47abf22", "3f8fab01d9c26fe052015fe7a547bb3e", "xg6g8gjfjuoicvlpjkri"]
}

images = []
for label, imgs in labels.items():
    for img in imgs:
        images.append(f"{label}/{img}")

fig, axs = plt.subplots(3, 4)
for i, ax in enumerate(axs.flatten()):
    ax.imshow(Image.open(f"{ROOT}/{images[i]}"))
    ax.axis("off")
plt.tight_layout()
plt.subplots_adjust(wspace=-0.15, hspace=0.05)
plt.savefig(f"{OUTPUT_LOCATION}/varied_images.pdf", bbox_inches="tight", pad_inches=0, dpi=150)
plt.close()
