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

print(menu())
wybor = input(" Wybierz funkcję : ");
x=input("Podaj x: ")
y=input("Podaj y: ")

if wybor == 1:
    print(x,"+",y, dodaj(x,y))
elif choice == 2:
    print (x,"-",y, odejmij(x,y))
