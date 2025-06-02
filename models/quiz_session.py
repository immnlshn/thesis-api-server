from typing import List, Dict
from pydantic import BaseModel
from .question import Question

class QuizSession(BaseModel):
    questions: List[Question]
    answers: Dict[str, str] = {}
