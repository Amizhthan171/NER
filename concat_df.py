from pdf2image import convert_from_path
import pytesseract

def ocr_pdf(pdf_path):
    text = ""
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        page_text = pytesseract.image_to_string(image, lang='eng')
        text += page_text + "\n"

    return text

pdf_path = "/path/to/your/pdf_file.pdf"
extracted_text = ocr_pdf(pdf_path)
print(extracted_text)