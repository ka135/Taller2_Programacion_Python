total_minutos = 0
tramo = 1

while True:
    tiempo_tramo = int(input(f'Ingresa el tiempo del tramo {tramo} en minutos (0 para terminar): '))

    if tiempo_tramo == 0:
        break

    total_minutos += tiempo_tramo
    tramo += 1

horas = total_minutos // 60
minutos = total_minutos % 60

print(f'El tiempo total del viaje es: {horas}:{minutos}')
