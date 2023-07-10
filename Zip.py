import fitz
import os

def convert_tiff_to_pdf(tiff_path):
    pdf_path = os.path.splitext(tiff_path)[0] + ".pdf"

    doc = fitz.open(tiff_path)
    pdf_bytes = doc.convert_to_pdf()

    with open(pdf_path, "wb") as output_pdf:
        output_pdf.write(pdf_bytes)

    os.remove(tiff_path)
    os.rename(pdf_path, tiff_path)

# Usage example
convert_tiff_to_pdf("example.tiff")