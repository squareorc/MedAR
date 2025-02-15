from fastapi import FastAPI
from ocr.ocr import extract_text_from_image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to MedAR API"}

@app.post("/ocr/")
def process_image():
    text = extract_text_from_image(r"C:\Users\harsh\OneDrive\Desktop\MedAR\static\sample.jpg")  # Make sure this file exists
    return {"extracted_text": text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
