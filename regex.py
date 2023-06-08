import pytesseract
import re

# Load the input image
image_path = "path/to/your/image.jpg"

# Perform OCR using pytesseract and generate hOCR output
hocr_data = pytesseract.image_to_pdf_or_hocr(image_path, extension='hocr')

# Specify the output file path
output_file = "path/to/output/file.hocr"

# Save the hOCR data to a file
with open(output_file, 'wb') as f:
    f.write(hocr_data)

print("hOCR file saved successfully.")