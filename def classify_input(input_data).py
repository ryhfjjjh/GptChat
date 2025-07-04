def classify_input(input_data):
    if type(input_data) == str and input_data.endswith('?'):
        return "qa"
    elif input_data.endswith(".wav"):
        return "speech"
    elif input_data.endswith(".jpg") or input_data.endswith(".png"):
        return "image"
    elif "өлең" in input_data.lower():
        return "poem"
    else:
        return "unknown"
