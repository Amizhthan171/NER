import PyPDF2
import fitz  # PyMuPDF

def has_images(page):
    # Implement the has_images function as shown in step 2.

def print_pages_with_images(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]

        # Convert the PyPDF2 page to PyMuPDF page
        pdf_document = fitz.open(pdf_file)
        mu_page = pdf_document.load_page(page_num)

        if has_images(mu_page):
            print(f"Page {page_num + 1} in {pdf_file} contains images.")

        pdf_document.close()

# Example usage:
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
for pdf_file in pdf_files:
    print_pages_with_images(pdf_file)