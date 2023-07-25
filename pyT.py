from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import numpy as np

def is_logo_or_text_image(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Check if the image contains any text using OCR (Tesseract)
    text = pytesseract.image_to_string(grayscale_image)
    if text.strip():
        return True

    # Convert the image to numpy array
    image_np = np.array(image)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2HSV)

    # Define color range for logos (you may need to adjust these values based on your logos)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])

    # Create masks for red and blue colors
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Combine the masks to detect red and blue colors in the image (logos are often red or blue)
    logo_mask = red_mask + blue_mask

    # Count the number of non-zero pixels in the logo mask
    num_logo_pixels = np.count_nonzero(logo_mask)

    # If a significant number of pixels are detected as logos, consider it a logo-based image
    if num_logo_pixels > 0.1 * image_np.size:
        return True

    return False

# Rest of the code remains the same