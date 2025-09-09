import matplotlib.pyplot as plt
import os
import random
from PIL import Image


ROOT = "../khana"
OUTPUT_LOCATION = "../docs/files/"

class_names = []
for class_name in sorted(os.listdir(ROOT)):
    if os.path.isdir(f"{ROOT}/{class_name}"):
        class_names.append(class_name)
num_classes = len(class_names)
num_images = 10

fig, axes = plt.subplots(num_classes, num_images + 1, figsize=(2 * (num_images + 1), 2 * num_classes))
plt.subplots_adjust(wspace=0.1, hspace=0.1)

for class_idx, class_name in enumerate(class_names):
    class_path = os.path.join(ROOT, class_name)
    if os.path.isdir(class_path):
        image_files = [os.path.join(class_path, f) for f in os.listdir(class_path)]
        selected = random.sample(image_files, min(num_images, len(image_files)))
        axes[class_idx, 0].axis('off')
        axes[class_idx, 0].text(0.5, 0.5, class_name, fontsize=14, ha='center', va='center')
        for i in range(num_images):
            ax = axes[class_idx, i + 1]
            ax.axis('off')
            if i < len(selected):
                img = Image.open(selected[i]).resize((64, 64), Image.Resampling.LANCZOS)
                ax.imshow(img)

plt.savefig(f"{OUTPUT_LOCATION}/browse.pdf", bbox_inches="tight", pad_inches=0.2, dpi=300)
plt.close()