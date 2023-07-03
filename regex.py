from pdf2image import convert_from_path
from PIL import Image

# Assuming you have the PDF file path
pdf_path = "path/to/your/file.pdf"

# Convert the PDF to images
images = convert_from_path(pdf_path)

# Iterate over the dataframe rows
for index, row in df.iterrows():
    # Extract the page number
    page_no = row['PAGE NO']

    # Get the specific page image
    page_image = images[page_no]

    # Extract the bounding box values
    bbox = row['BBOX']
    x_min, y_min, x_max, y_max = bbox

    # Crop the image based on the bounding box values
    cropped_image = page_image.crop((x_min, y_min, x_max, y_max))

    # Save the cropped image as a new file using the key name
    key_name = row['KEY']
    output_path = f"cropped_{key_name}.jpg"
    cropped_image.save(output_path)