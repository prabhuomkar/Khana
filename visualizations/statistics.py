import os
import matplotlib.pyplot as plt


ROOT = "../khana"
OUTPUT_LOCATION = "../paper/figs"

lc = {}

for dir in os.listdir(ROOT):
    if os.path.isdir(f"{ROOT}/{dir}"):
        images = os.listdir(f"{ROOT}/{dir}")
        lc[dir] = len(images)
result = {k: v for k, v in sorted(lc.items(), reverse=True, key=lambda item: item[1])}
image_counts = [v for _, v in result.items()]
labels = result.keys()
total_images = sum(image_counts)
percentages = [(count / total_images) * 100 for count in image_counts]
average_count = int(total_images / len(labels))

plt.figure(figsize=(16, 8))
plt.rcParams["font.family"] = "Fira Code"
bars = plt.bar(labels, image_counts, color="#F8474A", width=0.4)
for bar, count, percentage in zip(bars, image_counts, percentages):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f"{count}",
             ha="center", va="bottom", rotation=45, fontsize=8)

ax = plt.gca()
ax.tick_params(axis="both", which="both", length=0)
ax.tick_params(axis="both", which="both", width=0)
plt.xlim(-1, len(labels))
plt.xticks(rotation=90)
plt.axhline(y=average_count, color="#4E4193", linestyle="dashed", label=f"Average Count: {average_count}")
plt.legend()
plt.tight_layout()
plt.savefig(f"{OUTPUT_LOCATION}/statistics.pdf", pad_inches=0, dpi=150)
plt.close()
