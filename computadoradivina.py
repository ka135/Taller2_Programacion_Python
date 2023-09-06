import random

print("Piensa en un número del 1 al 100")
print("Ingresa '<' si es menor, '>' si es mayor, o '=' si es correcto")
min_num = 1
max_num = 100
intentos = 0

while True:
    intento = random.randint(min_num, max_num)
    intentos += 1
    respuesta = input(f"¿Es {intento} tu número? ")

    if respuesta == "<":
        max_num = intento - 1
    elif respuesta == ">":
        min_num = intento + 1
    elif respuesta == "=":
        print(f"Adiviné el número {intento} en {intentos} intentos")
        break
    else:
        print("Solo puedes ingresar '<', '>', o '='")