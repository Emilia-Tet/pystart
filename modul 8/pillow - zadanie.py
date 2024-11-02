from PIL import Image
import os
from pathlib import Path

directory = r'E:\PROJECTS\pystart\modul 8\funny animals'

target_path = 'funny animals/resized'
if not os.path.exists(target_path):
    os.makedirs(target_path)

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        file_path = Path(dirpath) / filename

        im = Image.open(file_path)
        resized_img = im.resize((300, 300))
        save_path = os.path.join(target_path, filename)
        resized_img.save(save_path)



    