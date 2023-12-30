import pytesseract
from PIL import Image

# Set the path to the Tesseract OCR executable (update this path according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = './Images./a7q1.jpg'
image = Image.open(image_path)
image = image.convert('L')  # Convert to grayscale
image = image.point(lambda p: p > 200 and 255)
# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)