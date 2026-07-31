from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from app.schemas.blueprint_schema import BlueprintRequest
from app.schemas.blueprint_response import BlueprintResponse
from app.services.ollama_service import generate_blueprint

app = FastAPI(
    title="BlueprintAI",
    description="AI-Powered Software Requirement to System Blueprint Generator",
    version="1.0.0"
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

    # Normalize AI response
    if isinstance(result.get("functional_requirements"), str):
        result["functional_requirements"] = [
            item.strip()
            for item in result["functional_requirements"].replace("\n", ".").split(".")
            if item.strip()
        ]

    if isinstance(result.get("non_functional_requirements"), str):
        result["non_functional_requirements"] = [
            item.strip()
            for item in result["non_functional_requirements"].replace("\n", ".").split(".")
            if item.strip()
        ]

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