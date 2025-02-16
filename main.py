from fastapi import FastAPI, UploadFile, File
from ocr.ocr import extract_text_from_image, get_medicine_info
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Welcome to MedAR API"}

@app.post("/ocr/")
async def process_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text using OCR
    extracted_text = extract_text_from_image(file_path)

    if not extracted_text:
        return {"error": "No text detected in image"}

    # Fetch medicine info from API (Handles API blocking issue)
    try:
        medicine_info = get_medicine_info(extracted_text)
    except Exception as e:
        medicine_info = "Could not fetch medicine information. Please try again later."

    return {
        "extracted_text": extracted_text,
        "medicine_info": medicine_info
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
