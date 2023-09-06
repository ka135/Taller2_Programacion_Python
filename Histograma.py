positivos = 0
negativos = 0

print("Ingrese valores enteros y termine con un 0")
n = int(input())

while n != 0:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    n = int(input())

print("Positivos")
for i in range(positivos):
    print("*", end="")
print()

print("Negativos")
for i in range(negativos):
    print("*", end="")
