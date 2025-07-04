# kaz_analysis.py

def analyze_question(text):
    text = text.lower()

    if any(word in text for word in ["кім", "кімдер"]):
        return "person"
    elif any(word in text for word in ["не", "неге", "нені", "неде"]):
        return "definition"
    elif "қашан" in text:
        return "time"
    elif any(word in text for word in ["қайда", "қай жақта"]):
        return "location"
    elif "қанша" in text:
        return "quantity"
    elif any(word in text for word in ["қалай", "қандай"]):
        return "method"
    else:
        return "general"
