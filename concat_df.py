from pdf2image import convert_from_path
from PIL import Image

def convert_pdf_to_single_image(pdf_path):
    images = convert_from_path(pdf_path)

    # Get the dimensions of the first image
    width, height = images[0].size

    # Create a new blank image with the size of the combined pages
    combined_image = Image.new('RGB', (width, height * len(images)))

    # Merge all the pages into the new image
    for i, image in enumerate(images):
        combined_image.paste(image, (0, i * height))

    return combined_image

pdf_path = "/path/to/your/pdf_file.pdf"
output_image = convert_pdf_to_single_image(pdf_path)

# Save the combined image to disk
output_image.save("/path/to/output_image.jpg", "JPEG")