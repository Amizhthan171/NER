import fitz  # PyMuPDF

def has_images(page):
    # Load the page as an image
    image_list = page.get_images(full=True)

    # Check if the page contains images
    if len(image_list) > 0:
        return True
    else:
        return False