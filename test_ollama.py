import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:7b",
        "prompt": "Hello",
        "stream": False
    },
    timeout=30
)

print("Status:", response.status_code)
print(response.json())