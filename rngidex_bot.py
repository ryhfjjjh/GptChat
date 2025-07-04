# rngidex_bot.py

from gd10h_model import GD10HModel

class RnGidexBot:
    def __init__(self):
        print("RnGidex бот іске қосылды 🤖")
        self.model = GD10HModel([64, 128, 256])
    
    def chat(self):
        print("Сәлем! Мен RnGidex ботымын. Қалағаныңды сұра!")
        while True:
            user_input = input("Сіз: ")
            if user_input.lower() in ['шығу', 'exit', 'quit']:
                print("Кездескенше! 👋")
                break
            response = self.generate_response(user_input)
            print("RnGidex:", response)

    def generate_response(self, prompt):
        # Бұл жерде болашақта model-ді толық пайдаланамыз
        return f"Мен әлі үйреніп жатырмын, бірақ сіз: \"{prompt}\" деп сұрадыңыз."

# Басты орындаушы
if __name__ == "__main__":
    bot = RnGidexBot()
    bot.chat()
