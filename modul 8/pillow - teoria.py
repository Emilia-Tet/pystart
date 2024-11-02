# https://pillow.readthedocs.io/en/stable/

from PIL import Image
im = Image.open('flower.jpg')
thumbnail = im.resize((300, 300))
thumbnail.save('resized.jpg')