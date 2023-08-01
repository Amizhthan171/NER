import os
from PIL import Image
import PyPDF2
import io

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
    page_object = page['/Resources']['/XObject'].get_object()
    image_count = 0

    for x in page_object.values():
        if x['/Subtype'] == '/Image':
            image = x.get_object()
            image_data = image.get_data()
            image_bytes = io.BytesIO(image_data)
            img = Image.open(image_bytes)

            black_pixels, white_pixels = count_black_white_pixels(img)
            if black_pixels + white_pixels > threshold:
                image_count += 1

    return image_count > 0

def find_pages_with_images(pdf_file):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)

        pages_with_images = []
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            if has_images(page):
                pages_with_images.append(page_num + 1)

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