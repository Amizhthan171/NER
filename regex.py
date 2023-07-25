import fitz  # PyMuPDF
import cv2

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
            np_array = bytearray(image_data.samples)
            image_np = np.array(np_array, dtype=np.uint8).reshape(image_data.height, image_data.width, 3)

            # Convert the BGR image to RGB (OpenCV uses BGR by default)
            rgb_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

            # Convert the image to grayscale
            grayscale_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

            # Perform image processing to detect regions that likely contain images
            # You can adjust the parameters based on your PDFs' characteristics
            _, threshold_image = cv2.threshold(grayscale_image, 200, 255, cv2.THRESH_BINARY)

            # Find contours in the thresholded image
            contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # If any contours are found, consider the page to contain images
            if len(contours) > 0:
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