import pytesseract
import cv2

def ocr_table_with_structure(image_path):
    # Read the image and perform OCR to get the bounding box information
    image = cv2.imread(image_path)
    ocr_data = pytesseract.image_to_boxes(image)

    # Process the OCR data to extract table content and maintain the structure
    lines = ocr_data.strip().split('\n')
    table_data = {}
    for line in lines:
        _, x, y, w, h, _ = line.split()
        row = int(y)
        if row not in table_data:
            table_data[row] = []
        table_data[row].append(line)

    # Sort the table_data by rows
    sorted_rows = sorted(table_data.keys())

    # Extract text for each row and align the columns
    table_content = []
    for row in sorted_rows:
        row_content = table_data[row]
        row_content.sort(key=lambda x: int(x.split()[1]))  # Sort by X-coordinate
        row_text = ' '.join(item.split()[0] for item in row_content)
        table_content.append(row_text)

    return table_content

# Specify the path to your image containing the table
image_path = 'path_to_your_image.png'

# Get the table content while preserving the structure
table_content = ocr_table_with_structure(image_path)

# Print the extracted table content
for row in table_content:
    print(row)