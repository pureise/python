code = input("Podaj nowy kod blokady: ")
access = False
while access == False:
    unlock = input("Podaj kod do odlbokowania: ")
    if unlock == code:
        access = True
        print("kod poprawny, zamek otworzony")
    else:
        print("kod niepoprawny")
        
