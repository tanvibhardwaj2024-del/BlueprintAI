import json
import requests

from app.prompts.module_generation_prompt import MODULE_GENERATION_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b"


def generate_module_code(files, blueprint):

    prompt = MODULE_GENERATION_PROMPT.format(
        blueprint=json.dumps(blueprint, indent=2),
        files="\n".join(files)
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

    response_text = response.json()["response"].strip()

    return json.loads(response_text)