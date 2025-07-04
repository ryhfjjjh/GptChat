def generate_response_with_context(full_context: str) -> str:
    full_context = full_context.lower()  # барлығын кіші әріпке айналдырамыз

    # Кейбір негізгі үлгілер бойынша жауаптар
    if "абай" in full_context and "кім" in full_context:
        return "Абай Құнанбаев — қазақтың ұлы ойшылы, ақыны және ағартушысы."
    
    elif "тәуелсіздік" in full_context and "қай жылы" in full_context:
        return "Қазақстан тәуелсіздігін 1991 жылы 16 желтоқсанда алды."

    elif "астанасы" in full_context or "астана" in full_context:
        return "Қазақстанның астанасы — Астана қаласы (бұрынғы Нұр-Сұлтан)."

    elif "алгоритм" in full_context and "не" in full_context:
        return "Алгоритм — нақты бір мәселені шешуге бағытталған іс-әрекеттер тізбегі."

    elif "рахмет" in full_context:
        return "Сізге де көп рахмет! Қалағаныңызды сұрай беріңіз 😊"

    elif "қалайсың" in full_context or "қалың қалай" in full_context:
        return "Мен жасанды интеллектпін, бірақ сіздің көңіл күйіңіз қалай? 🙂"

    elif "әзіл" in full_context:
        return "Міне бір әзіл: Екі программист кафеде отыр. Бірі екіншісіне: «Сенде де баг бар ма?» дейді."

    # Егер ештеңе сәйкес келмесе
    else:
        return "Бұл сұраққа нақты жауап беруге қиналып тұрмын 🤔. Басқа қырынан сұрап көріңізші!"
