import os
import io
from PIL import Image
import fitz  # PyMuPDF

def count_black_white_pixels(image):
    # Function to count the number of black and white pixels in an image.
    black_pixels = white_pixels = 0
    for pixel in image.getdata():
        if pixel == (0, 0, 0):  # Black pixel
            black_pixels += 1
        elif pixel == (255, 255, 255):  # White pixel
            white_pixels += 1
    return black_pixels, white_pixels

def has_images(page, threshold=100):
    # Function to check if a page has images based on black and white pixel count.
    image_list = page.getImageList()
    image_count = 0

    for image in image_list:
        xref = image[0]
        base_image = page.get_image(xref)
        image_bytes = base_image.samples

        img = Image.open(io.BytesIO(image_bytes))

        black_pixels, white_pixels = count_black_white_pixels(img)
        if black_pixels + white_pixels > threshold:
            image_count += 1

    return image_count > 0

def find_pages_with_images(pdf_file):
    pdf_document = fitz.open(pdf_file)

    pages_with_images = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        if has_images(page):
            pages_with_images.append(page_num + 1)

    pdf_document.close()
    return pages_with_images

def process_directory(directory_path):
    # Function to process all PDFs in a directory and find pages with images.
    pdf_files = [f for f in os.listdir(directory_path) if f.endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory_path, pdf_file)
        pages_with_images = find_pages_with_images(pdf_path)
        print(f"File: {pdf_file} - Pages with images: {pages_with_images}")

# Replace 'pdf_directory_path' with the path to the directory containing the PDFs.
pdf_directory_path = "/path/to/your/pdf_directory"
process_directory(pdf_directory_path)