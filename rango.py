print("Cuantos datos desea ingresar")
n = int(input())
a = []

for i in range(n):
    print("Valor:", i + 1)
    a.append(float(input()))

min_value = min(a)
max_value = max(a)
res = max_value - min_value

print("El rango es", res)