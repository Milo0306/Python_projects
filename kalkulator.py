while True:
    dzialanie = input("Co chcesz zrobić?")
    if dzialanie == ("exit"):
        print("wychodzę z programu")
        break
    liczba1 = input("Podaj pierwszą liczbę:")
    if liczba1 == ("exit"):
        print("wychodzę z programu")
        break
    liczba2 = input("Podaj drugą liczbę:")
    if liczba2 == ("exit"):
        print("wychodzę z programu")
        break

    if liczba1.isdigit() and liczba2.isdigit():
        liczba1 = int(liczba1)
        liczba2 = int(liczba2)

        if dzialanie == "dodaj":
            print(liczba1 + liczba2)
        elif dzialanie == "odejmij":
            print(liczba1 - liczba2)
        elif dzialanie == "pomnóż":
            print(liczba1 * liczba2)
        elif dzialanie == "podziel":
            print(liczba1 / liczba2)
        else:
            print(
                "Podaj cyfry i wybierz jedną z opcji: dodaj, odejmij, pomnóż, podziel"
            )
    else:
        print("Musisz podać cyfry, inaczej Ci nie pomogę")
