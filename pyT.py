import PyPDF2

# Define the region of interest (ROI)
x0 = 100   # x-coordinate of the upper-left corner of the ROI
y0 = 100   # y-coordinate of the upper-left corner of the ROI
x1 = 200   # x-coordinate of the lower-right corner of the ROI
y1 = 200   # y-coordinate of the lower-right corner of the ROI

# Open the PDF file in read binary mode
with open('file.pdf', 'rb') as pdf_file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the page object for the first page of the PDF file
    page = pdf_reader.getPage(0)

    # Get the dimensions of the page
    page_width = page.mediaBox.getWidth()
    page_height = page.mediaBox.getHeight()

    # Define the ROI in PDF coordinates
    roi_x0 = x0 / page_width
    roi_y0 = 1 - (y1 / page_height)
    roi_x1 = x1 / page_width
    roi_y1 = 1 - (y0 / page_height)

    # Define a TextString object for the ROI
    roi = PyPDF2.pdf.TextString('')

    # Loop through each text object on the page
    for obj in page['/Contents'].getObject():

        # Check if the object is a TextString
        if isinstance(obj, PyPDF2.pdf.TextString):

            # Check if the TextString is within the ROI
            x, y = obj.getXY()
            if roi_x0 < x < roi_x1 and roi_y0 < y < roi_y1:
                roi += obj

    # Extract the text from the ROI
    text = roi.decode('utf-8')

    # Do something with the extracted text
    print(text)
