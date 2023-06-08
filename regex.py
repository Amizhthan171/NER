import pytesseract
import re
from PIL import Image

# Load the input image
image_path = "path/to/your/image.jpg"
image = Image.open(image_path)

# Convert the image to grayscale for better OCR accuracy
image_gray = image.convert("L")

# Perform OCR using pytesseract on the grayscale image
ocr_data = pytesseract.image_to_data(image_gray, output_type=pytesseract.Output.DICT)

# Assume you have already extracted the desired text using a regex
extracted_text = "Amount: $1234"

# Find the index of the desired text within the OCR results
text_index = None
for i, word in enumerate(ocr_data["text"]):
    if word == extracted_text:
        text_index = i
        break

# Retrieve the bounding box coordinates if the text is found
if text_index is not None:
    left = ocr_data["left"][text_index]
    top = ocr_data["top"][text_index]
    width = ocr_data["width"][text_index]
    height = ocr_data["height"][text_index]
    bounding_box = (left, top, left + width, top + height)
    print("Bounding box:", bounding_box)
else:
    print("Text not found in OCR results.")