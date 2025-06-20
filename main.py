from fastapi import FastAPI, File, UploadFile, Form
from PIL import Image
from model import predict_disease

app = FastAPI()

@app.post("/predict/")
async def diagnose(image: UploadFile = File(...), report: str = Form(...)):
    try:
        pil_image = Image.open(image.file)
        result = predict_disease(pil_image, report)
        return {"prediction": result}
    except Exception as e:
        print("🔥 Error during prediction:", e)
        return {"error": str(e)}
