import google.generativeai as genai
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import os


load_dotenv()
# Set up Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_image(image_path):
    """Extracts text (medicine name) from the given image."""
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text.strip()

def get_medicine_info(medicine_name):
    """Fetches medicine details from Gemini API based on the extracted name."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt =  f"Provide safe and general medical information about {medicine_name}. Do not include any dangerous content."
    response = model.generate_content(prompt)

    if not response.candidates or not response.candidates[0].content.parts:
        return "No valid response from API. The request might have been blocked."
    return response.text

# Example Usage
if __name__ == "__main__":
    img_path = r"C:\Users\harsh\OneDrive\Desktop\MedAR\static\sample.jpg"  # Change this to your image path
    extracted_text = extract_text_from_image(img_path)
    print("Extracted Medicine Name:", extracted_text)

    if extracted_text:
        medicine_info = get_medicine_info(extracted_text)
        print("Medicine Details from Gemini:\n", medicine_info)
