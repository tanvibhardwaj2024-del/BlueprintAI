import os

from app.services.ai_code_generator import generate_ai_code


def create_files(file_structure, blueprint):

    base_path = "../generated_project"

    created_files = []

    for file in file_structure:

        file_path = os.path.join(base_path, file)

        folder = os.path.dirname(file_path)

        os.makedirs(folder, exist_ok=True)

        print(f"Generating {file}...")

        try:
            code = generate_ai_code(file, blueprint)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)

            created_files.append(file_path)

        except Exception as e:
            print(f"Failed: {file}")
            print(e)

    print("\n===== CREATED FILES =====")
    for file in created_files:
        print(file)

    return created_files