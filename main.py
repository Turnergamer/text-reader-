import pytesseract
import pyperclip
from PIL import Image
import os
from PIL import ImageFilter, ImageOps

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Path to screenshot image
img_path = "/home/neilj/Code/Type speed discord/screenshot/test.png"

# Open image and convert to grayscale
img = Image.open(img_path).convert("L")
img = img.point(lambda x: 0 if x < 128 else 255)

# Apply blurring to smooth out edges
img = img.filter(ImageFilter.GaussianBlur(radius=2))

# Invert the image to make the text stand out
img = ImageOps.invert(img)
# Use Tesseract to extract text from image
text = pytesseract.image_to_string(img, config='--psm 6')

# Copy text to clipboard
pyperclip.copy(text)
print(text)
# Delete screenshot image
#os.remove(img_path)The man saw how big the strawberry was and he
