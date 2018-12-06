with open('plik.txt', 'r') as file:
    with open('doZapisu.txt', 'w') as toSave:
        i = 0
        for line in file:
            i += 1
            print(str(i) + " " + line)
