import requests
import json
import re

from app.prompts.blueprint_prompt import BLUEPRINT_PROMPT
from app.services.project_generator import generate_project

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"

def generate_blueprint(requirement: str):

    final_prompt = BLUEPRINT_PROMPT.format(
        requirement=requirement
    )

    print("\n===== FINAL PROMPT =====")
    print(final_prompt)
    print("========================\n")

    payload = {
        "model": MODEL_NAME,
        "prompt": final_prompt,
        "stream": False
    }

    try:

        print("Sending request to Ollama...")

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=900
        )

        print("Status Code:", response.status_code)

        response.raise_for_status()

        ollama_response = response.json()

        print("\n===== RAW RESPONSE =====")
        print(ollama_response)
        print("========================")

        # Clean markdown from Ollama response
        response_text = ollama_response["response"].strip()

        response_text = re.sub(
            r"^```json\s*|\s*```$",
            "",
            response_text,
            flags=re.DOTALL
        ).strip()

        # Convert JSON string into Python dictionary
        data = json.loads(response_text)

        # Fill missing keys
        data.setdefault("project_summary", "")
        data.setdefault("functional_requirements", "")
        data.setdefault("non_functional_requirements", "")
        data.setdefault("tech_stack", {})
        data.setdefault("database_tables", [])
        data.setdefault("api_endpoints", [])
        data.setdefault("sql_schema", [])
        data.setdefault("folder_structure", [])
        data.setdefault("modules", [])

        # Generate project (folders + files + code + zip)
        zip_file = generate_project(data)

        # Add zip file path to response
        data["zip_file"] = zip_file

        print("\n===== FINAL DATA =====")
        print(data)
        print("======================")

        return data

    except Exception as e:

        print("\n========== FULL ERROR ==========")

        import traceback
        traceback.print_exc()

        print("================================")

        return {
            "project_summary": "",
            "functional_requirements": "",
            "non_functional_requirements": "",
            "tech_stack": {},
            "database_tables": [],
            "api_endpoints": [],
            "sql_schema": [],
            "folder_structure": [],
            "modules": [],
            "zip_file": None,
            "error": str(e)
        }