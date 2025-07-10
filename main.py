from fastapi import FastAPI, HTTPException
import json
import uuid

from typing import Dict

from models.answer_input import AnswerInput
from models.question import Question
from models.quiz_session import QuizSession

with open("./data/questions.json", "r", encoding="utf-8") as f:
  questions = [Question(**q) for q in json.load(f)]

app = FastAPI()
sessions: Dict[str, QuizSession] = {}

@app.get("/quiz/start")
def start_quiz():
  session_id = str(uuid.uuid4())
  session = QuizSession(
      sessionId=session_id,
      questions=questions,
      answerInputs=[]
  )
  sessions[session_id] = session
  return {
    "sessionId": session_id, "questions": [{
      "id": q.id,
      "text": q.text,
      "answers": [{"id": a.id, "text": a.text} for a in q.answers]
    } for q in questions]
  }


@app.post("/quiz/{session_id}/answer")
def submit_answer(session_id: str, payload: AnswerInput):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="SESSION_NOT_FOUND")

    question = next((q for q in session.questions if q.id == payload.questionId), None)
    if question is None:
        raise HTTPException(status_code=400, detail="Invalid question ID")

    if not hasattr(session, "answerInputs") or session.answerInputs is None:
        session.answerInputs = []
    session.answerInputs.append(payload)
    return {"correct": payload.answerId == question.correctAnswerId}

@app.get("/quiz/{session_id}/result")
def get_result(session_id: str):
    session = sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="SESSION_NOT_FOUND")
    # Mapping von questionId zu answerId aus answerInputs
    answers = {a.questionId: a.answerId for a in getattr(session, "answerInputs", [])}
    score = sum(
        1 for q in session.questions
        if answers.get(q.id) == q.correctAnswerId
    )
    return {
        "score": score,
        "total": len(session.questions),
        "correctAnswers": [{"questionId": q.id, "answerId": q.correctAnswerId} for q in session.questions]
    }

