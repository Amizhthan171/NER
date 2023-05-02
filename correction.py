import PyPDF2

# Open the PDF file
with open('example.pdf', 'rb') as pdf_file:
    # Create a PdfFileReader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()

    # Loop over each page and extract the text
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        print(page_text)
