from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import whisper
import os
from services.transcription import transcribe_audio
from services.symptom_checker import check_symptoms
from services.drug_interaction import check_interaction

app = FastAPI(title="AI Service", description="AI-powered healthcare services")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_path = f"temp_{file.filename}"
    with open(audio_path, "wb") as buffer:
        buffer.write(await file.read())
    
    result = transcribe_audio(audio_path, model)
    os.remove(audio_path)
    return {"transcription": result}

@app.post("/symptom-check")
async def symptom_check(data: dict):
    symptoms = data.get("symptoms", "")
    result = check_symptoms(symptoms)
    return result

@app.post("/drug-interaction")
async def drug_interaction(data: dict):
    drugs = data.get("drugs", [])
    result = check_interaction(drugs)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)