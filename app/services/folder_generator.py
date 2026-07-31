import os


def create_project_structure(folder_structure):
    created_folders = []

    base_path = "../generated_project"

    os.makedirs(base_path, exist_ok=True)

    for folder in folder_structure:
        path = os.path.join(base_path, folder)

        os.makedirs(path, exist_ok=True)

        created_folders.append(path)

    print("Created folders:", created_folders)

    return created_folders