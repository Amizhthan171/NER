import PyPDF2
import re
from datetime import datetime

# Open the PDF file in read binary mode
with open('file.pdf', 'rb') as pdf_file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the page object for the first page of the PDF file
    page = pdf_reader.getPage(0)

    # Extract the text from the page as a string
    page_text = page.extractText()

    # Search for a date string in the page text using regular expressions
    date_regex = r'[A-Z][a-z]{2}\s\d{1,2},\s\d{4}'  # Example regular expression for "May 1, 2023"
    match = re.search(date_regex, page_text)

    if match:
        # Convert the date string to a datetime object
        date_str = match.group(0)
        date_obj = datetime.strptime(date_str, '%B %d, %Y')

        # Do something with the datetime object
        print(date_obj)
    else:
        print("Date not found.")
