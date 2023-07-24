import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def has_images(pdf_file):
    pdf_document = fitz.open(pdf_file)
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        for img in images:
            img_data = page.get_image_data(img[0])
            img_bytes = img_data["image"]

            # Convert the image bytes to a PIL image
            pil_image = Image.open(img_bytes)
            text = pytesseract.image_to_string(pil_image)

            # You can improve the accuracy by analyzing the OCR text or implementing more complex rules
            if text.strip():
                return True

    return False

def print_pages_with_images(pdf_file):
    if has_images(pdf_file):
        print(f"At least one page in {pdf_file} contains images.")
    else:
        print(f"No pages in {pdf_file} contain images.")

# Example usage:
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
for pdf_file in pdf_files:
    print_pages_with_images(pdf_file)