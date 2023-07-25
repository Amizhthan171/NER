import fitz  # PyMuPDF

def has_large_images(pdf_file):
    pdf_document = fitz.open(pdf_file)
    pages_with_large_images = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        for _, img in images.items():  # Iterate through the images
            image_width, image_height = img[0], img[1]
            if image_width > 600 and image_height > 460:
                pages_with_large_images.append(page_num + 1)
                break  # Break the loop if any large image is found on the page

    pdf_document.close()
    return pages_with_large_images

def print_pages_with_large_images(pdf_file):
    pages_with_large_images = has_large_images(pdf_file)
    if pages_with_large_images:
        print(f"The following page(s) in {pdf_file} contain large images: {pages_with_large_images}.")
    else:
        print(f"No pages in {pdf_file} contain large images.")

# Example usage:
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
for pdf_file in pdf_files:
    print_pages_with_large_images(pdf_file)