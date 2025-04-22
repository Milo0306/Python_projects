while True:
    liczba = input("Podaj liczbę, sprawdzimy czy jest parzysta: ")
    if liczba == "exit":
        break
    if not liczba.isdigit(): 
         print("podaj poprawną wartość")
         continue
    liczba = int(liczba)
    if liczba % 2 == 0:
        print("patrzysta")
    else:
        print('nieparzysta')