from app.services.folder_generator import create_project_structure
from app.services.file_generator import create_files
from app.services.zip_generator import create_zip


def generate_project(data):

    # Create folders
    create_project_structure(data["folder_structure"])

    # Generate files list
    files = []

    for module in data["modules"]:

        name = module.lower().replace(" ", "_")

        files.extend([
            f"backend/routes/{name}_routes.py",
            f"backend/controllers/{name}_controller.py",
            f"backend/services/{name}_service.py",
        ])

    # Common files
    files.extend([
        "backend/database/database.py",
        "backend/config/config.py",
        "frontend/pages/Home.jsx",
        "frontend/components/Navbar.jsx"
    ])

    # AI generates ONE file at a time
    create_files(files, data)

    # Create ZIP
    zip_file = create_zip()

    print(f"ZIP Created: {zip_file}")

    return zip_file