def menu():
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")

def dodaj(x,y):
    return x + y

def odejmij(x,y):
    return x - y

def pomnoz(x,y):
    return x * y

def podziel(x,y):
    if (y == 0):
        print("Nigdy cholero nie dziel przez zero")
        return x / y

menu()

wybor = input(" Wybierz funkcję : ")

x = float(input("Podaj x: "))

y = float(input("Podaj y: "))

if wybor == '1':
    print(x,"+",y,"=", dodaj(x,y))
elif wybor == '2':
    print(x,"-",y,"=", odejmij(x,y))
elif wybor == '3':
    print(x,"*",y,"=", pomnoz(x,y))
elif wybor == '4':
    print(x,"/",y,"=", podziel(x,y))

