# rngidex_bot.py

from kaz_analysis import analyze_question
from kaz_response import generate_response
from gd10h_model import GD10HModel

# GD10H моделін инициализациялау
model = GD10HModel([64, 128, 256])  # Қабаттар қажетіне қарай өзгерт

print("\n🤖 RnGidex іске қосылды! Сұрағыңызды қазақ тілінде қойыңыз:")

while True:
    user_input = input("👤 Сіз: ")
    
    if user_input.lower() in ["шығу", "тоқта", "exit", "quit"]:
        print("🤖 RnGidex: Сау болыңыз! 👋")
        break

    qtype = analyze_question(user_input)
    response = generate_response(qtype)

    print("🤖 RnGidex:", response)
