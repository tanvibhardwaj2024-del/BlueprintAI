from typing import List
from pydantic import BaseModel

from app.schemas.tech_stack_schema import TechStack
from app.schemas.database_table_schema import DatabaseTable
from app.schemas.api_endpoint_schema import ApiEndpoint
from app.schemas.sql_schema import SQLSchema

class BlueprintResponse(BaseModel):
    project_summary: str

    functional_requirements: List[str]
    non_functional_requirements: List[str]

    tech_stack: TechStack

    database_tables: List[DatabaseTable]

    api_endpoints: List[ApiEndpoint]

    sql_schema: List[SQLSchema]

    folder_structure: List[str]

    modules: List[str]