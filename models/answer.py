from pydantic import BaseModel

class Answer(BaseModel):
    id: str
    text: str
