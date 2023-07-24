import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import cv2
import numpy as np

def has_images(pdf_file):
    pdf_document = fitz.open(pdf_file)
    pages_with_images = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        for img in images:
            xref = img[0]
            image_data = page.get_pixmap(xref=xref)

            # Convert the image data to a NumPy array for OpenCV processing
            np_array = np.frombuffer(image_data.samples, dtype=np.uint8).reshape(image_data.height, image_data.width, 3)

            # Convert the BGR image to RGB (OpenCV uses BGR by default)
            bgr_image = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)

            # Convert the image to grayscale for OCR
            grayscale_image = cv2.cvtColor(bgr_image, cv2.COLOR_RGB2GRAY)

            # Perform OCR on the image
            text = pytesseract.image_to_string(Image.fromarray(grayscale_image))

            # Check if the page contains images based on OCR result
            if text.strip():
                pages_with_images.append(page_num + 1)
                break  # Break the loop if any image is found on the page

    return pages_with_images

def print_pages_with_images(pdf_file):
    pages_with_images = has_images(pdf_file)
    if pages_with_images:
        print(f"The following page(s) in {pdf_file} contain images: {pages_with_images}.")
    else:
        print(f"No pages in {pdf_file} contain images.")

# Example usage:
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
for pdf_file in pdf_files:
    print_pages_with_images(pdf_file)