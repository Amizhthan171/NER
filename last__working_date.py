import camelot
import PyPDF4

def read_pdf_with_pypdf4(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF4.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages
        text = ""
        for page_number in range(num_pages):
            page = pdf_reader.getPage(page_number)
            text += page.extract_text()
    return text

pdf_path = 'path/to/your/pdf_file.pdf'
pdf_text = read_pdf_with_pypdf4(pdf_path)
tables = camelot.read_pdf(pdf_text)