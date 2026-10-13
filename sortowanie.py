def wczytaj_dane():
    plik = open("uczniowie.txt","r",encoding="utf-8")
    dane = plik.readlines()
    plik.close

    for i in range(len(dane)):
        dane[i] = dane[i].strip()

    return dane

def wyswietl_dane(dane):
    print("\nDane: ")

    for element in dane:
        print(element)

def posortuj_dane(dane):
    sort = dane.copy()
    sort.sort(key=str.lower)

    plik = open("uczniowie_posortowane.txt","w",encoding="utf-8")

    for element in sort:
        plik.write(element + "\n")

    plik.close()

    print("\nUczniowie zostli posortowani alfabetycznie")

def usun_ucznia(dane):
    if not dane:
        print("Lista uczniów jest pusta.")
        return

    print("\nLista uczniów:")
    for i,uczen in enumerate(dane,start=1):
        print(f"{i}.{uczen}")

    try:
        numer = int(input("Podaj numer ucznia do usuniecia"))

        if 1 <= numer <= len(dane):
            usuniety = dane.pop(numer - 1)
            print(f"Usunięto ucznia: {usuniety}")
        else:
            print("Nieprawidłowy numer ucznia")
    
    except ValueError:
        print("Podaj poprawny numer")

def menu(dane):
    while True:
        print("1. Wświetl liste uczniów")
        print("2. Posortuj listę alfabetycznie")
        print("3. Usuń ucznia z listy")
        print("4. Zakończ program")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            wyswietl_dane(dane)
        elif wybor == "2":
            posortuj_dane(dane)
        elif wybor == "3":
            usun_ucznia(dane)
        elif wybor == "4":
            print("Koniec programu")
            break
        else:
            print("Nieprawidłowa opcja")

def main():
    dane = wczytaj_dane()
    menu(dane)

main()