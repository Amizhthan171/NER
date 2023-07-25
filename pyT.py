import PyPDF4
from PIL import Image

def is_logo_or_text_image(image):
    # Check if the image contains any text or has high saturation
    # You can customize the filtering criteria based on your specific use case
    # For simplicity, we'll use a basic filtering approach here

    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Calculate the pixel intensity histogram
    histogram = grayscale_image.histogram()

    # If more than 95% of the pixels have a low intensity (text-based image)
    if sum(histogram[:64]) / float(image.size[0] * image.size[1]) > 0.95:
        return True

    # If the image has high saturation (logo-based image)
    saturation = image.convert("HSV").split()[1].histogram()
    if sum(saturation[-64:]) / float(image.size[0] * image.size[1]) > 0.3:
        return True

    return False

def has_large_images(pdf_file):
    pages_with_large_images = []

    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF4.PdfFileReader(file)

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            resources = page['/Resources']
            if '/XObject' in resources:
                xObject = resources['/XObject']
                for obj in xObject:
                    obj_stream = xObject[obj]
                    if obj_stream['/Subtype'] == '/Image':
                        image = Image.open(obj_stream.get_object())
                        width, height = image.size
                        if width > 600 and height > 460 and not is_logo_or_text_image(image):
                            pages_with_large_images.append(page_num + 1)
                            break  # Break the loop if any large suitable image is found on the page

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