from pydantic import BaseModel

from app.schemas.tech_stack_schema import TechStack
from app.schemas.database_table_schema import DatabaseTable
from app.schemas.api_endpoint_schema import ApiEndpoint
from app.schemas.sql_schema import SQLSchema


class BlueprintResponse(BaseModel):
    project_summary: str

    functional_requirements: list[str]

    non_functional_requirements: list[str]

    tech_stack: TechStack

    database_tables: list[DatabaseTable]

    api_endpoints: list[ApiEndpoint]

    sql_schema: list[SQLSchema]

    folder_structure: list[str]

    file_structure: list[str]

    modules: list[str]

    zip_file: str