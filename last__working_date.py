import camelot
import fitz

def read_pdf_with_pymupdf(pdf_path):
    pdf_text = ""
    with fitz.open(pdf_path) as pdf_document:
        num_pages = pdf_document.page_count
        for page_number in range(num_pages):
            page = pdf_document[page_number]
            pdf_text += page.get_text()
    return pdf_text

pdf_path = 'path/to/your/pdf_file.pdf'
pdf_text = read_pdf_with_pymupdf(pdf_path)
tables = camelot.read_pdf(pdf_text)