import pytesseract
import cv2

# Set the Tesseract path (only needed for Windows users)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return "Error: Image not found."

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)
    return text

# Test OCR when running ocr.py directly
if __name__ == "__main__":
    result = extract_text_from_image(r"C:\Users\harsh\OneDrive\Desktop\MedAR\static\sample.jpg")  # Make sure 'sample.jpg' exists
    print("Extracted Text:", result)
