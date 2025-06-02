from pydantic import BaseModel

class AnswerInput(BaseModel):
  questionId: str
  answerId: str