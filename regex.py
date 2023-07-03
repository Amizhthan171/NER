from PIL import Image

# Assuming you have the image path
image_path = "path/to/your/image.jpg"

# Load the image
image = Image.open(image_path)

# Iterate over the dataframe rows
for index, row in df.iterrows():
    # Extract the bounding box values
    bbox = row['BBOX']
    x_min, y_min, x_max, y_max = bbox

    # Crop the image based on the bounding box values
    cropped_image = image.crop((x_min, y_min, x_max, y_max))

    # Save the cropped image using the key name
    key_name = row['KEY']
    cropped_image.save(f"cropped_{key_name}.jpg")