laberinto = [
    ['E', 'C', 'C', 'C', 'P', 'C' , 'C'],
    ['P', 'C', 'C', 'C', 'P', 'C' , 'C'],
    ['C', 'C', 'C', 'C', 'C', 'C' , 'C'],
    ['C', 'C', 'C', 'C', 'C', 'C' , 'C'],
    ['C', 'C', 'C', 'C', 'C', 'C' , 'C'],
    ['P', 'P', 'P', 'C', 'C', 'P' , 'C'],
    ['C', 'C', 'P', 'C', 'C', 'C' , 'S']
]


movimientos = [(-2, 0), (2, 0), (0, -3), (0, 3)]


entrada = None
salida = None
for i in range(len(laberinto)):
    for j in range(len(laberinto[i])):
        if laberinto[i][j] == 'E':
            entrada = (i, j)
        elif laberinto[i][j] == 'S':
            salida = (i, j)


pila = [(entrada, [entrada])]
caminos = []

while pila:
    posicion_actual, camino = pila.pop()
    x, y = posicion_actual


    if posicion_actual == salida:
        caminos.append(camino)
        continue

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and laberinto[nx][ny] in ['C', 'S']:
            if (nx, ny) not in camino:
                pila.append(((nx, ny), camino + [(nx, ny)]))

print("Caminos hacia la salida:")
for i, camino in enumerate(caminos, 1):
    print(f"Camino {i}: {camino}")
