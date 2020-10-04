def clear():

    def func(line):
        new = list(line)
        index = 0
        for char in line:
            if char == "#":
                new[index] = ''
            elif char == "-":
                new[index] = ''
            index = index + 1
        a = ''.join(new)
        return a
    def lenght(line):
        len_ = 0
        for letter in line:
            if letter != " ":
                len_ = len_ + 1
        return len_

    with open("text.txt", "r") as f:
        lines = f.readlines()

    with open("text.txt", "w") as f:
        for line in lines:
           
           if lenght(line) > 20:
                f.write(line)
    
    with open ("text.txt", "r") as f:
        lines = f.readlines()
    
    bene = dict()
    with open ("text.txt", "w") as f:
        for line in lines:
            if not bene.get(func(line)):
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
        correct_symbols = {'\n', ' ', '.', ':', '-', '?', '!', ',', '#'}
        for char in line:
            if char.isdigit() or char in correct_symbols or (ord(char)>=ord('а')-32 and ord(char) <= ord('а')+31) or (ord(char)>=ord('a') and ord(char)<=ord('z')) or (ord(char)>=ord('A') and ord(char)<=ord('Z')):
                continue
            return 0
        return 1
    correctChars()
clear()
