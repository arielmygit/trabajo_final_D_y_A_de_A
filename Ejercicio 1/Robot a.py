# Las coordenadas estan dadas por: (2fila,3columna)
# O(1)
laberinto = [
    # 0    1    2    3    4    5    6    7    8    9
    ['E', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #0
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #1
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #2
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #3
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #4
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #5
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #6
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #7
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #8
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #9
    ['P', 'C', 'C', 'P', 'C', 'C', 'C', 'C', 'C', 'C'], #10
    ['P', 'C', 'C', 'P', 'C', 'C', 'C', 'C', 'C', 'C'], #11
    ['P', 'C', 'C', 'P', 'C', 'C', 'C', 'C', 'C', 'C'], #12
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #13
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'], #14
    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'S']  #15
]

movimientos = [(1, 0), (0, -3), (2, 0), (0,3)]


def es_valido(x, y, visitado):
    # O(1)
    return (0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and
            laberinto[x][y] != 'P' and not visitado[x][y])


def buscar_salida(inicio):
    pila = [inicio]  # O(1)
    visitado = [[False] * len(laberinto[0]) for _ in range(len(laberinto))]  # O(n*m)
    visitado[inicio[0]][inicio[1]] = True  # O(1)

    while pila:  # O(n*m)
        x, y = pila[-1]  # O(1)
        if laberinto[x][y] == 'S':  # O(1)
            return list(pila)

        movido = False
        for dx, dy in movimientos:  # O(4)
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny, visitado):
                pila.append((nx, ny))
                visitado[nx][ny] = True
                movido = True
                break

        if not movido:
            pila.pop()  # O(1)

    return []


for i in range(len(laberinto)):  # O(n)
    for j in range(len(laberinto[i])):  # O(m)
        if laberinto[i][j] == 'E':  # O(1)
            camino = buscar_salida((i, j))
            if camino:
                print("Camino a la salida encontrado:", camino)  # O(1)
            else:
                print("No hay camino a la salida.")  # O(1)
            break

# O(14) + O(n*m) + O(n*m) + O(n*m) = O(3(n*m))
# O(n*m) <- Peor de los casos


