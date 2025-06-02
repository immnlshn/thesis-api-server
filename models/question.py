from typing import List
from pydantic import BaseModel
from .answer import Answer

class Question(BaseModel):
    id: str
    text: str
    answers: List[Answer]
    correctAnswerId: str
