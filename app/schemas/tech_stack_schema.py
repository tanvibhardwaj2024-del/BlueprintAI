from pydantic import BaseModel

class TechStack(BaseModel):
    frontend: str
    backend: str
    database: str
    deployment: str
    cloud: str