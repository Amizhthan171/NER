import pytesseract
import re
from PIL import Image

# Load the input image
image_path = "path/to/your/image.jpg"
image = Image.open(image_path)

# Convert the image to grayscale for better OCR accuracy
image_gray = image.convert("L")

# Perform OCR using pytesseract on the grayscale image
ocr_text = pytesseract.image_to_string(image_gray)

# Assume you have already extracted the desired text using a regex
extracted_text = "Amount: $1234"

# Find the index of the desired text within the OCR results
match = re.search(re.escape(extracted_text), ocr_text)
if match:
    start_index = match.start()
    end_index = match.end()

    # Iterate over the OCR text to find the bounding box
    left = top = width = height = 0
    char_count = 0
    for i, char in enumerate(ocr_text):
        if char_count == start_index:
            left = i
        if char_count == end_index - 1:
            width = i - left + 1
            height = 1
            break
        if char != '\n':
            char_count += 1

    # Calculate the top coordinate based on line breaks
    lines = ocr_text.split('\n')
    line_count = 0
    for line in lines:
        if char_count <= len(line):
            top = line_count
            break
        else:
            char_count -= len(line) + 1
            line_count += 1

    # Construct the bounding box coordinates
    bounding_box = (left, top, left + width, top + height)
    print("Bounding box:", bounding_box)
else:
    print("Text not found in OCR results.")