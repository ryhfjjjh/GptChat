def detect_language(text):
    if any("\u4e00" <= c <= "\u9fff" for c in text):
        return "chinese"
    elif any("а" <= c <= "я" for c in text.lower()):
        return "russian"
    elif any(c in text.lower() for c in "қңғүұәөһі"):
        return "kazakh"
    return "english"
