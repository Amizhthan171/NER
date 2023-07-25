import PyPDF4
from PIL import Image

def has_large_images(pdf_file):
    pages_with_large_images = []

    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF4.PdfFileReader(file)

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            resources = page['/Resources']
            if '/XObject' in resources:
                xObject = resources['/XObject'].get_object()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        width = xObject[obj]['/Width']
                        height = xObject[obj]['/Height']
                        if width > 600 and height > 460:
                            pages_with_large_images.append(page_num + 1)
                            break  # Break the loop if any large image is found on the page

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