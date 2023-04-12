import pytesseract
import pyperclip
from PIL import Image
import os
from PIL import ImageFilter, ImageOps

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

img_path = "/home/neilj/Downloads/test.png"

img = Image.open(img_path).convert("L")

img = ImageOps.invert(img)
text = pytesseract.image_to_string(img, config='--psm 6')

text = text.replace('\n', ' ')

pyperclip.copy(text)
print(text)
