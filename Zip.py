from PIL import Image
import pandas as pd

def crop_and_save_images(tiff_path, dataframe):
    image = Image.open(tiff_path)

    for index, row in dataframe.iterrows():
        page_no = row['page no']
        bbox = row['bbox']
        field = row['field']

        # Convert bbox coordinates to integers
        bbox = [int(coord) for coord in bbox]

        # Crop the image using the bbox coordinates
        image_page = image.copy()
        image_page.seek(page_no)
        cropped_image = image_page.crop(bbox)

        # Save the cropped image with the field name as a JPEG
        save_path = f"{field}.jpg"
        cropped_image.save(save_path, "JPEG")

# Usage example
df = pd.DataFrame({
    'page no': [0, 0, 1, 1],
    'bbox': [(100, 100, 300, 300), (200, 200, 400, 400), (150, 150, 350, 350), (250, 250, 450, 450)],
    'field': ['field1', 'field2', 'field3', 'field4']
})

tiff_file = "example.tiff"

crop_and_save_images(tiff_file, df)