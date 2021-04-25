def menu():
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")

def dodaj(x,y):
    wynik=x+y
    return wynik
print(menu())
wybor = input(" Wybierz funkcję : ");
x=input("Podaj x: ")
y=input("Podaj y: ")
if wybor == 1:
    print(dodaj(x,y))