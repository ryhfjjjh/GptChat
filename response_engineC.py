def generate_response_with_context(full_context: str) -> str:
    context = full_context.lower()

    # Қазақша
    if "күн жүйесі" in context:
        return "Күн жүйесі — 8 планета және Күн."

    # English (Standard + American)
    elif "solar system" in context:
        return "The solar system consists of 8 planets orbiting the Sun."

    elif "pythagorean" in context:
        return "Pythagorean theorem: a² + b² = c²."

    elif "speed" in context:
        return "Speed formula: v = s / t."

    # Russian
    elif "солнечная система" in context:
        return "Солнечная система состоит из 8 планет и Солнца."

    elif "теорема пифагора" in context:
        return "Теорема Пифагора: a² + b² = c²."

    # Chinese (Simplified)
    elif "太阳系" in context:
        return "太阳系有八大行星围绕太阳运行。"

    elif "毕达哥拉斯" in context or "勾股定理" in context:
        return "勾股定理：a² + b² = c²。"

    else:
        return "Сұрағыңызды нақтылап жазыңыз немесе басқа тілде қайталап көріңіз."
