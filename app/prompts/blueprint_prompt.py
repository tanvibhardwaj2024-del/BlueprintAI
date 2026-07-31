BLUEPRINT_PROMPT = """
You are a Senior Software Architect.

Requirement:
{requirement}

Return ONLY valid JSON.

The JSON MUST contain ALL of these fields.

{{
  "project_summary":"...",
  
  "functional_requirements":"...",

  "non_functional_requirements":"...",

  "tech_stack": {{
      "frontend":"...",
      "backend":"...",
      "database":"...",
      "deployment":"...",
      "cloud":"..."
  }},

  "database_tables":[
    {{
      "table_name":"Users",
      "columns":[
        "id",
        "name",
        "email"
      ]
    }}
  ],

  "api_endpoints":[
    {{
      "method":"GET",
      "endpoint":"/users",
      "description":"Get all users"
    }},
    {{
      "method":"POST",
      "endpoint":"/users",
      "description":"Create a new user"
    }}
  ],

  "sql_schema":[
    {{
      "table_name":"Users",
      "create_query":"CREATE TABLE Users (id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100));"
    }}
  ],

  "folder_structure":[
    "backend/",
    "backend/controllers/",
    "backend/routes/",
    "backend/services/",
    "backend/models/",
    "backend/database/",
    "backend/utils/",
    "backend/config/",
    "frontend/",
    "frontend/components/",
    "frontend/pages/",
    "frontend/services/",
    "frontend/assets/"
  ],

  "file_structure":[
    "backend/routes/example_route.py",
    "backend/controllers/example_controller.py",
    "backend/services/example_service.py",
    "backend/models/example_model.py",
    "backend/database/database.py",
    "frontend/pages/Home.jsx",
    "frontend/components/Navbar.jsx"
],

  "modules":[
    "Authentication",
    "User Management",
    "Product Management"
  ]
}}

Rules:

1. Return all fields.
2. tech_stack must be a JSON object.
3. database_tables must be a list of objects.
4. api_endpoints must be a list of objects.
5. sql_schema must be a list of objects.
6. folder_structure must be a list of folder paths.
7. file_structure must be a list of file paths.
8. Generate file_structure according to the selected technology stack.
9. Include important backend and frontend files only.
10. Do not generate code inside file_structure.
11. modules must be a list of strings.
12. create_query must contain a valid SQL CREATE TABLE statement.
13. Return ONLY valid JSON.
14. Do not use markdown.
15. Do not explain anything.
"""