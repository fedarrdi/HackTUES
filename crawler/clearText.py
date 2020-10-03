def clear():
    with open("text.txt", "r") as f:
        lines = f.readlines()

    with open("text.txt", "w") as f:
        for line in lines:
            if len(line) > 20:
                f.write(line)
    
    with open ("text.txt", "r") as f:
        lines = f.readlines()

    bene = dict()
    with open ("text.txt", "w") as f:
        for line in lines:
            if not bene.get(line):
                bene[line] = True
                f.write(line)

def correctLines():
    def correctChars():
        with open("text.txt", "r") as f:
            lines = f.readlines()
        with open("text.txt", "w") as f:
            for line in lines:
                if currLineAvailable(line, f):
                    f.write(line)
                else:
                    continue

    def currLineAvailable(line, f):
        correct_letters = { 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'ь', 'Ю', 'ю', 'Я', 'я', 'ѝ', '\n', ' ', '.', ':', '-', '?', '!'}
        for char in line:
            if char.isdigit() or char in correct_letters:
                continue
            else:
                 return 0
        return 1

    correctChars()
    correctLines()
