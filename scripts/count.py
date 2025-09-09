import os


ROOT = "../khana"

lc = {}
count = 0

for dir in os.listdir(ROOT):
    if os.path.isdir(f"{ROOT}/{dir}"):
        images = os.listdir(f"{ROOT}/{dir}")
        lc[dir] = len(images)
        count += lc[dir]

result = {k: v for k, v in sorted(lc.items(), key=lambda item: item[1])}
print(result)
print(f"Labels: {len(result.items())}")
print(f"Images: {count}")