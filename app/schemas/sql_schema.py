from pydantic import BaseModel


class SQLSchema(BaseModel):
    table_name: str
    create_query: str