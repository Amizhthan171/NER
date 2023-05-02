import pdf2image
import pytesseract

# Load PDF page 3
pdf_file = 'document.pdf'
page_number = 3
page_image = pdf2image.convert_from_path(pdf_file, first_page=page_number, last_page=page_number)[0]

# Extract text from page image
page_text = pytesseract.image_to_string(page_image, lang='eng')

# Find the date in the text
date = None
for word in page_text.split():
    if word.endswith(('th', 'st', 'nd', 'rd')):
        try:
            date = datetime.strptime(word, '%d%b%Y')
            break
        except ValueError:
            pass

# Print the date
if date is not None:
    print('Found date:', date.strftime('%Y-%m-%d'))
else:
    print('Date not found.')
