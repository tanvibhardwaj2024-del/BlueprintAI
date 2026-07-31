MODULE_GENERATION_PROMPT = """
You are a Senior Software Engineer.

Project Blueprint:
{blueprint}

Generate complete code for the following files:

{files}

Return ONLY valid JSON.

Example:

{{
  "backend/routes/authentication_routes.py": "<complete code>",
  "backend/controllers/authentication_controller.py": "<complete code>",
  "backend/services/authentication_service.py": "<complete code>"
}}

Rules:
1. Return ONLY JSON.
2. Keys must be file paths.
3. Values must contain complete code.
4. Do not use markdown.
5. Do not explain anything.
"""