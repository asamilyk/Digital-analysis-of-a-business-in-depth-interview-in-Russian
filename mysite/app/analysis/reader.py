def read(file):
    with open(file, 'r', encoding='utf-8') as file:
        lines = file.read()
        return lines
