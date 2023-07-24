import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def has_images(pdf_file):
    pdf_document = fitz.open(pdf_file)
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        for img in images:
            xref = img[0]
            image_data = page.get_pixmap(xref=xref)

            pil_image = Image.frombytes("RGB", [image_data.width, image_data.height], image_data.samples)

            # Convert the PIL image to grayscale for OCR (optional but can be helpful)
            grayscale_image = pil_image.convert('L')

            # Perform OCR on the image
            text = pytesseract.image_to_string(grayscale_image)

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