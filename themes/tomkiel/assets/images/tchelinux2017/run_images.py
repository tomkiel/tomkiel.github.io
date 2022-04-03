from PIL import Image, ImageEnhance
import os

app_root = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(app_root)

for file in files:
    if file.endswith(".png") or file.endswith(".jpeg"):
        picture = Image.open(file)
        addjust = ImageEnhance.Brightness(picture).enhance(1.2)
        addjust = ImageEnhance.Color(addjust).enhance(0.8).save(file.replace(".jpeg", ".jpg"))
        print(file.replace(".jpeg", ".jpg"))
