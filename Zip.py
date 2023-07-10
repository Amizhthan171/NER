import img2pdf
import os

def convert_tiff_to_pdf(tiff_path):
    pdf_path = os.path.splitext(tiff_path)[0] + ".pdf"
    with open(pdf_path, "wb") as output_pdf:
        output_pdf.write(img2pdf.convert(tiff_path))

    os.remove(tiff_path)
    os.rename(pdf_path, tiff_path)

# Usage example
convert_tiff_to_pdf("example.tiff")