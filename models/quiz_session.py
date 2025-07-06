from typing import List
from pydantic import BaseModel

from .answer_input import AnswerInput
from .question import Question

class QuizSession(BaseModel):
    sessionId: str
    questions: List[Question]
    answerInputs: List[AnswerInput]
