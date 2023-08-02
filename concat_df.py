import pytesseract
from PIL import Image

# Perform OCR on the table image to extract the table structure
def ocr_table(image_path):
    image = Image.open(image_path)
    # Use --psm 6 for sparse text with OSD (Page Segmentation Mode)
    # Use --psm 11 for sparse text
    extracted_data = pytesseract.image_to_osd(image, config='--psm 6')
    return extracted_data

# OCR the table image and get the structured table data
# Replace "path/to/your/table_image.jpg" with the path to your table image file
table_data = ocr_table("path/to/your/table_image.jpg")

# Print the structured table data
print(table_data)