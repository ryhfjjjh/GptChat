from knowledge_base import get_answer
from language_router import detect_language

def generate_response_with_context(question):
    # Пән мен сұрақтың тақырыбын анықтаймыз
    q_lower = question.lower()

    if "пифагор" in q_lower or "pythagorean" in q_lower:
        return "Пифагор теоремасы: тік бұрышты үшбұрышта гипотенузаның квадраты катеттердің квадраттарының қосындысына тең. Формуласы: a² + b² = c²"

    elif "күш" in q_lower or "force" in q_lower or "ньютон" in q_lower:
        return "Ньютонның екінші заңы: Денеге әсер ететін күш оның массасы мен үдеуі көбейтіндісіне тең. Формуласы: F = ma"

    elif "жер шар" in q_lower or "earth" in q_lower:
        return "Жер шары — Күн жүйесіндегі тіршілік бар жалғыз планета. Ол Күннен үшінші орында орналасқан."

    elif "су формуласы" in q_lower or "water formula" in q_lower or "h2o" in q_lower:
        return "Судың химиялық формуласы — H₂O. Ол екі сутек пен бір оттек атомынан тұрады."

    elif "биология" in q_lower and "жасуша" in q_lower:
        return "Жасуша — тірі организмнің ең кіші құрылымдық және қызметтік бірлігі."

    elif "жаратылыстану" in q_lower and "атмосфера" in q_lower:
        return "Атмосфера — Жерді қоршап тұрған газ қабаты, ол тіршілік үшін өте маңызды."

    # Егер нақты пән табылмаса
    return "Сұрағыңыз қабылданды. Қосымша нақты пән мен тақырыпты көрсетсеңіз, мен нақтырақ жауап беремін ✅"
