from gd10h_model import GD10HModel
from response_engine import generate_response_with_context

# Модельді бастау (формалды)
model = GD10HModel([64, 128, 256])

print("\n🤖 RnGidex іске қосылды! Сұрағыңызды кез келген тілде жазыңыз:")

while True:
    user_input = input("👤 Сіз: ")

    if user_input.lower() in ["шығу", "тоқта", "exit", "quit"]:
        print("🤖 RnGidex: Сау болыңыз! 👋")
        break

    response = generate_response_with_context(user_input)
    print("🤖 RnGidex:", response)
