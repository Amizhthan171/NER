import PyPDF2

# Assuming you have the PDF file path
pdf_path = "path/to/your/file.pdf"

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_path)

# Iterate over the dataframe rows
for index, row in df.iterrows():
    # Extract the page number
    page_no = row['PAGE NO']

    # Get the page object from the PDF reader
    page = pdf_reader.getPage(page_no)

    # Extract the bounding box values
    bbox = row['BBOX']
    x_min, y_min, x_max, y_max = bbox

    # Crop the page based on the bounding box values
    cropped_page = page.crop((x_min, y_min, x_max, y_max))

    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # Add the cropped page to the PDF writer
    pdf_writer.addPage(cropped_page)

    # Save the cropped page as a new PDF file using the key name
    key_name = row['KEY']
    output_path = f"cropped_{key_name}.pdf"
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)