import os
import torch
import random
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


ROOT = "../khana"
OUTPUT_LOCATION = "../paper/figs"

transform = transforms.Compose([
    transforms.ToTensor(),
])

samples = []

for dir in os.listdir(ROOT):
    if dir != ".DS_Store":
        images = os.listdir(f"{ROOT}/{dir}")
        random_image = random.choice(images)
        samples.append(transform(Image.open(f"{ROOT}/{dir}/{random_image}")))

img_grid = torchvision.utils.make_grid(samples, nrow=10)
npimg = img_grid.numpy()
plt.imshow(np.transpose(npimg, (1, 2, 0)))
plt.axis("off")
plt.savefig(f"{OUTPUT_LOCATION}/heading.pdf", bbox_inches="tight", pad_inches=0, dpi=300)
plt.close()
