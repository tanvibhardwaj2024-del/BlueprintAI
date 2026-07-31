import os
import shutil


def create_zip():

    project_folder = "../generated_project"

    zip_name = "generated_project"

    shutil.make_archive(
        zip_name,
        "zip",
        project_folder
    )

    return zip_name + ".zip"