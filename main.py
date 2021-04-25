#Przydatna biblioteka w tego typu projektach
import math

def menu():
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Pierwiastkowanie")

def dodaj(x,y):
    return x + y

def odejmij(x,y):
    return x - y

def pomnoz(x,y):
    return x * y

def podziel(x,y):
    return x / y

def poteguj(x,y):
    return x ** y

menu()

wybor = input(" Wybierz funkcję : ")

if wybor == '1':
    while True:
        try:
            x = float(input("Podaj liczbę x: "))
            y = float(input("Podaj liczbę y: "))
            x + y
            break
        except ValueError:
            print('Podaj poprawne wartości!')
            continue
    print(x, "+", y, "=", dodaj(x, y))
elif wybor == '2':
    while True:
        try:
            x = float(input("Podaj liczbę x: "))
            y = float(input("Podaj liczbę y: "))
            x - y
            break
        except ValueError:
            print('Podaj poprawne wartości!')
            continue
    print(x,"-",y,"=", odejmij(x,y))
elif wybor == '3':
    while True:
        try:
            x = float(input("Podaj liczbę x: "))
            y = float(input("Podaj liczbę y: "))
            x * y
            break
        except ValueError:
            print('Podaj poprawne wartości!')
            continue
    print(x, "*", y, "=", pomnoz(x, y))
elif wybor == '4':
    while True:
        try:
            x = float(input("Podaj liczbę a którą chcesz podzielić: "))
            y = float(input("Podaj dzielnik: "))
            x / y
            break
        except ValueError:
            print('Podaj poprawne wartości!')
            continue

        except ZeroDivisionError:
            print('Nigdy cholero nie dziel przez zero!')
            continue
    print(x, "/", y, "=", podziel(x, y))
elif wybor == '5':
    while True:
        try:
            x = float(input("Podaj podstawę potęgi: "))
            y = float(input("Podaj wykładnik: "))
            x ** y
            break
        except ValueError:
            print('Podaj poprawne wartości!')
            continue
    print(x, "**", y, "=", poteguj(x, y))
else:
    print("Wybierz prawidłową opcję!")
