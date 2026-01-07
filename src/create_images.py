from PIL import Image
import os

base_path = "data/images/train"
os.makedirs(base_path, exist_ok=True)

colors = [
    (120, 180, 200),
    (100, 160, 180),
    (80, 140, 160),
    (60, 120, 140),
    (40, 100, 120)
]

for i in range(5):
    img = Image.new("RGB", (256, 256), colors[i])
    img.save(f"{base_path}/house_{i}.png")

print("STEP 7 DONE: 5 satellite images created")
