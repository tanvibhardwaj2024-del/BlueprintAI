from pydantic import BaseModel


class ApiEndpoint(BaseModel):
    method: str
    endpoint: str
    description: str