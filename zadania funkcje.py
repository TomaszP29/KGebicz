print("Zadanie1:")
def pole_prostokata(dlugosc, szerokosc):
  return dlugosc * szerokosc

print(pole_prostokata(5,3))

print("\n")
print("Zadanie 2:")

def uczen(imie, wiek=18):
  return f"Uczeń {imie} ma {wiek} lat"

print(uczen("Jan",17))
print(uczen("Adam"))

print("\n")
print("Zadanie 3:")

def dodaj(a,b):
  return a+b

def odejmij(a,b):
  return a-b

def pomnoz(a,b):
  return a*b

def podziel(a,b):
  return a/b

print(dodaj(10,5))
print(odejmij(10,5))
print(pomnoz(10,5))
print(podziel(10,5))

print("\n")
print("Zadanie 4:")

def cena_biletu(wiek,cena_podstawowa=30):
  if wiek < 13:
    return 15
  elif wiek < 18:
    return 20
  else:
    return cena_podstawowa

print(cena_biletu(10))
print(cena_biletu(15))
print(cena_biletu(25))

print("\n")
print("Zadanie 5:")

def produkt(nazwa,cena,sztuk):
  wartosc = cena*sztuk
  return f"{nazwa}: {wartosc}zł"

print(produkt("Laptop",3500,2))
print(produkt("Telefon",2000,3))
print(produkt("Myszka",100,5))