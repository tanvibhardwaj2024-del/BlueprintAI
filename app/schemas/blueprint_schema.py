from pydantic import BaseModel

class BlueprintRequest(BaseModel):
    requirement: str