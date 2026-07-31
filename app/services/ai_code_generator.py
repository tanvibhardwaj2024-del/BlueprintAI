import json
import requests

from app.prompts.code_generation_prompt import CODE_GENERATION_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b"


def generate_ai_code(file_name, blueprint):

    prompt = CODE_GENERATION_PROMPT.format(
        blueprint=json.dumps(blueprint, indent=2),
        file_name=file_name
    )

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=900
    )

    response.raise_for_status()

    return response.json()["response"].strip()