import fitz  # PyMuPDF

def has_images(pdf_file):
    pdf_document = fitz.open(pdf_file)
    pages_with_images = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        for img in images:
            xref = img[0]
            image_data = page.get_pixmap(xref=xref)

            # Check if the image has color channels other than grayscale
            if image_data.n - image_data.alpha > 1:
                pages_with_images.append(page_num + 1)
                break  # Break the loop if any colored image is found on the page

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