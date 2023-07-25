from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2

def is_logo_or_text_image(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Check if the image contains any text using OCR (Tesseract)
    text = pytesseract.image_to_string(grayscale_image)
    if text.strip():
        return True

    # Check if the image has high saturation (logo-based image)
    image_cv2 = cv2.cvtColor(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2HSV)
    saturation = image_cv2[..., 1]
    saturation_mean = saturation.mean()
    if saturation_mean > 150:  # You can adjust the threshold value based on your needs
        return True

    return False

def has_large_images(pdf_file):
    pages_with_large_images = []

    images = convert_from_path(pdf_file, dpi=300)  # Convert PDF pages to images

    for page_num, image in enumerate(images):
        width, height = image.size
        if width > 600 and height > 460 and not is_logo_or_text_image(image):
            pages_with_large_images.append(page_num + 1)

    return pages_with_large_images

def print_pages_with_large_images(pdf_file):
    pages_with_large_images = has_large_images(pdf_file)
    if pages_with_large_images:
        print(f"The following page(s) in {pdf_file} contain large suitable images: {pages_with_large_images}.")
    else:
        print(f"No pages in {pdf_file} contain large suitable images.")

# Example usage:
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
for pdf_file in pdf_files:
    print_pages_with_large_images(pdf_file)