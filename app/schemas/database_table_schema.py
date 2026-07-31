from pydantic import BaseModel
from typing import List


class DatabaseTable(BaseModel):
    table_name: str
    columns: List[str]