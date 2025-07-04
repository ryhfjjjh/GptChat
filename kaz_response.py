
# kaz_response.py

def generate_response(question_type):
    if question_type == "person":
        return "Бұл адамға қатысты сұрақ. Мысалы: Абылай хан, Абай Құнанбаев т.б."
    elif question_type == "definition":
        return "Бұл анықтама сұрауы. Мысалы: сөздің мағынасы."
    elif question_type == "time":
        return "Бұл уақытқа байланысты сұрақ. Мысалы: 1991 жылы."
    elif question_type == "location":
        return "Бұл орын жайлы сұрақ. Мысалы: Қазақстанда, Астанада."
    elif question_type == "quantity":
        return "Бұл сан сұрауы. Мысалы: 5 адам, 10 жыл."
    elif question_type == "method":
        return "Бұл тәсіл жайлы сұрақ. Мысалы: қалай жұмыс істейді?"
    else:
        return "Сұрағыңызды түсіндім, нақты ақпарат бере аламын!"
