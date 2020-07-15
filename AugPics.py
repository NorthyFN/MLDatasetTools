import os
from PIL import Image, ImageEnhance
import random

MAIN_DIR = input("Directory: ")
MAIN_DIR = MAIN_DIR.replace("\\", "/")
if not os.path.isdir(MAIN_DIR):
    print("Directory not found.")
    exit()
OUT_DIR = input("Output directory: ")
OUT_DIR = OUT_DIR.replace("\\", "/")
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
    print("Created output directory.")
num_Aug = input("Number of saved augmentation: ")
try:
    num_Aug = abs(int(num_Aug))
except:
    print("Input not an integer.")
    exit()

counter = 0
for file in os.listdir(MAIN_DIR):
    fEnding = os.path.splitext(file)
    if fEnding[len(fEnding) - 1] == ".jpg":
        image = Image.open(f"{MAIN_DIR}/{file}")
        counter += 1
        for a in range(num_Aug):
            randRed = random.uniform(0.6,1.4)
            randGreen = random.uniform(0.6,1.4)
            randBlue = random.uniform(0.6,1.4)
            source = image.split()
            r = source[0].point(lambda i: i * randRed)
            g = source[1].point(lambda i: i * randGreen)
            b = source[2].point(lambda i: i * randBlue)

            out = Image.merge("RGB", (r, g, b))
            out = ImageEnhance.Contrast(out).enhance(random.uniform(0.5, 1.5))
            out = ImageEnhance.Sharpness(out).enhance(random.uniform(0.7, 2))
            out.save(f"{OUT_DIR}/{os.path.splitext(file)[0]}.aug({a}).jpg")
            # print(f"{os.path.splitext(file)[0]}.aug({a}).jpg")

print(f"Saved {counter * num_Aug} augmented images.")

