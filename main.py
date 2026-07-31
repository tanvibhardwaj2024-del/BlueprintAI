from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.blueprint_schema import BlueprintRequest
from app.schemas.blueprint_response import BlueprintResponse
from app.services.ollama_service import generate_blueprint

app = FastAPI(
    title="BlueprintAI",
    description="AI-Powered Software Requirement to System Blueprint Generator",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to BlueprintAI 🚀"
    }

@app.post("/generate", response_model=BlueprintResponse)
def generate(request: BlueprintRequest):

    print("========== STEP 1 ==========")
    print("Endpoint reached")
    print("Requirement:", request.requirement)

    result = generate_blueprint(request.requirement)

    print("========== STEP 2 ==========")
    print(result)

    return result
@app.get("/download")
def download_project():

    zip_path = "generated_project.zip"

    if os.path.exists(zip_path):
        return FileResponse(
            path=zip_path,
            filename="generated_project.zip",
            media_type="application/zip"
        )

    return {
        "error": "ZIP file not found"
    }