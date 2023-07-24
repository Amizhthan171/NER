import PyPDF2
from pdf2image import convert_from_path
from PIL import Image

def has_images(page_image):
    # Convert the page_image to grayscale for better analysis (optional but can be helpful)
    grayscale_image = page_image.convert('L')

    # Threshold the image to binarize it (optional but can be helpful)
    threshold_value = 200
    threshold_image = grayscale_image.point(lambda p: p > threshold_value and 255)

    # Count the number of non-white pixels in the image
    num_non_white_pixels = sum(1 for pixel in threshold_image.getdata() if pixel < 255)

    # You can adjust the threshold for the number of non-white pixels based on your requirements
    # Here, we set a simple threshold of 100 non-white pixels to qualify as having an image
    if num_non_white_pixels > 100:
        return True
    else:
        return False

def print_pages_with_images(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page_image = convert_from_path(pdf_file, first_page=page_num+1, last_page=page_num+1)[0]

        if has_images(page_image):
            print(f"Page {page_num + 1} in {pdf_file} contains images.")

# Example usage:
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
for pdf_file in pdf_files:
    print_pages_with_images(pdf_file)