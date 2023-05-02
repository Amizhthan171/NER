import pytesseract
from PIL import Image

# Load image
img = Image.open('image.jpg')

# Define the region containing the date (top left corner)
x = 0
y = 0
width = 200
height = 50
date_region = (x, y, x+width, y+height)

# Extract the date text from the region
date_text = pytesseract.image_to_string(img.crop(date_region), lang='eng', config='--psm 6')

# Print the extracted date text
print(date_text)
