# gf67_api.py

from fastapi import FastAPI
from pydantic import BaseModel
from kaz_analysis import analyze_question
from kaz_response import generate_response
from gd10h_model import GD10HModel

app = FastAPI()

# GD10H моделін дайындау (бір рет қана)
model = GD10HModel([64, 128, 256])  # Қабаттар өзіңізге байланысты

# Пайдаланушы сұрағының құрылымы
class UserQuestion(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: UserQuestion):
    qtype = analyze_question(data.question)
    answer = generate_response(qtype)
    return {"answer": answer}
