import numpy as np
import time
import matplotlib.pyplot as plt


# Métodos de ordenamiento
def burbuja(arr):
    n = len(arr) #O(1)
    for i in range(n): #O(n^2)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  #O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #O(1)
#Complejidad: O(3 + n^2) = O(n^2)


def insercion(arr):
    for i in range(1, len(arr)): #O(n^2)
        e = arr[i] #O(1)
        j = i - 1 #O(1)
        while j >= 0 and e < arr[j]:
            arr[j + 1] = arr[j] #O(1)
            j -= 1 #O(1)
        arr[j + 1] = e #O(1)
#Complejidad: O(5 + n^2) = O(n^2)


def seleccion(arr):
    n = len(arr)  #O(1)
    for i in range(n): #O(n^2)
        min_idx = i #O(1)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: #O(1)
                min_idx = j #O(1)
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #O(1)
#Complejidad: O(5 + n^2) = O(n^2)


def mezcla(arr):
    if len(arr) > 1: #O(1)
        mid = len(arr) // 2 #O(1)
        L, R = arr[:mid], arr[mid:] #O(n)
        mezcla(L) #O(n log n)
        mezcla(R)

        i = j = k = 0 #O(1)
        while i < len(L) and j < len(R): #O(n)
            if L[i] < R[j]: #O(1)
                arr[k] = L[i] #O(1)
                i += 1 #O(1)
            else:
                arr[k] = R[j] #O(1)
                j += 1 #O(1)
            k += 1 #O(1)

        while i < len(L): #O(n)
            arr[k] = L[i] #O(1)
            i += 1 #O(1)
            k += 1 #O(1)

        while j < len(R): #O(n)
            arr[k] = R[j] #O(1)
            j += 1 #O(1)
            k += 1 #O(1)
#Complejidad: O(14+n+n+n+4n+nlogn) = O(nlogn)


# Funciones auxiliares
def generar_numeros_aleatorios(cantidad):
    números_aleatorios = np.random.randint(1, 100000, size=cantidad)
    with open('numeros_aleatorios.txt', 'w') as file:
        file.writelines(f"{n}\n" for n in números_aleatorios)
    return números_aleatorios


def guardar_lista_ordenada_final(lista, nombre_archivo="lista_ordenada_final.txt"):
    with open(nombre_archivo, 'w') as file:
        file.writelines(f"{n}\n" for n in lista)


def medir_tiempo_ordenamiento(metodo, numeros):
    copia = numeros.copy()
    start_time = time.time()
    metodo(copia)
    elapsed_time = time.time() - start_time
    return copia, elapsed_time


# Bucle principal
cantidad_inicial = 0
incremento = 100000
max_cantidad = 100000

metodos = [mezcla]
tiempos_por_metodo = {metodo.__name__: [] for metodo in metodos}
cantidades = range(cantidad_inicial, max_cantidad + 1, incremento)

for cantidad in cantidades:
    numeros = generar_numeros_aleatorios(cantidad)

    for metodo in metodos:
        lista_ordenada, tiempo = medir_tiempo_ordenamiento(metodo, numeros)
        tiempos_por_metodo[metodo.__name__].append(tiempo)
        print(f"Tiempo de {metodo.__name__} para {cantidad} números: {tiempo:.6f} segundos")

    guardar_lista_ordenada_final(lista_ordenada)

# Graficar los resultados
for metodo, tiempos in tiempos_por_metodo.items():
    plt.plot(list(cantidades), tiempos, label=metodo)

plt.xlabel('Cantidad de números')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de cada método de ordenamiento')
plt.legend()
plt.show()
