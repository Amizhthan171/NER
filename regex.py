import fitz

# Assuming you have the PDF file path
pdf_path = "path/to/your/file.pdf"

# Open the PDF file
pdf_file = fitz.open(pdf_path)

# Iterate over the dataframe rows
for index, row in df.iterrows():
    # Extract the page number
    page_no = row['PAGE NO']

    # Get the specific page from the PDF
    page = pdf_file[page_no]

    # Extract the bounding box values
    bbox = row['BBOX']
    x_min, y_min, x_max, y_max = bbox

    # Crop the page based on the bounding box values
    cropped_page = page.crop((x_min, y_min, x_max, y_max))

    # Save the cropped page as a new PDF file using the key name
    key_name = row['KEY']
    output_path = f"cropped_{key_name}.pdf"
    cropped_page.save(output_path, garbage=3, deflate=True, clean=True)

# Close the PDF file
pdf_file.close()