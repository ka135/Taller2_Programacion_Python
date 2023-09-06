import random

intrandomNumber = random.randint(1, 100)
min_value = 0
max_value = 100
contador = 0

while True:
    n = int(input(f"Ingrese su número entre {min_value} y {max_value}: "))
    contador += 1

    if n <= min_value or n >= max_value:
        print("PERDIO")
        break

    if n == intrandomNumber:
        print("Felicitaciones")
        break
    else:
        if n > intrandomNumber:
            max_value = n
            print("EL NÚMERO ES MENOR")
        else:
            min_value = n
            print("EL NÚMERO ES MAYOR")

    print(f"Intentos: {contador}")

if n == intrandomNumber:
    print("Felicitaciones")