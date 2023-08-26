def formatName(string):
    string = string.strip()
    return ' '.join([item.capitalize() for item in string.split()])