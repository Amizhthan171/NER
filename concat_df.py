import pytesseract
from PIL import Image
import PyPDF2

# Perform OCR on the image/PDF to extract text
def ocr_image(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        extracted_text = ""
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            extracted_text += page.extractText()
    return extracted_text

# OCR the document to get the extracted text
# Replace "path/to/your/image.jpg" with the path to your image file or
# "path/to/your/document.pdf" with the path to your PDF file
# Uncomment one of the below lines based on the document type.
# extracted_text = ocr_image("path/to/your/image.jpg")  # For images (JPEG)
# extracted_text = extract_text_from_pdf("path/to/your/document.pdf")  # For PDFs

# Preprocess the extracted text to handle empty columns
def preprocess_text_for_empty_columns(extracted_text):
    # Replace blank columns with "0 dollars"
    lines = extracted_text.split("\n")
    modified_lines = []
    for line in lines:
        # Split the line by tabs (assuming columns are separated by tabs)
        columns = line.split("\t")
        modified_columns = []
        for column in columns:
            # If the column is empty or contains only whitespace, replace with "0 dollars"
            if not column.strip():
                modified_columns.append("0 dollars")
            else:
                modified_columns.append(column)
        # Join the modified columns back into a line
        modified_line = "\t".join(modified_columns)
        modified_lines.append(modified_line)

    # Join the modified lines back into the preprocessed text
    preprocessed_text = "\n".join(modified_lines)
    return preprocessed_text

# Preprocess the OCR extracted text to handle empty columns
preprocessed_text = preprocess_text_for_empty_columns(extracted_text)

# Now you can use the preprocessed text in the GPT-3.5 prompt
# and proceed with the rest of the code for extracting values using GPT-3.5 API.