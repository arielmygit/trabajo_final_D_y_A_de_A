# Modificamos el algoritmo de ordenamiento por insersion, usando una busqueda binaria
def insertion_sort(datos):
    for n in range(1,len(datos)): # O(n²)
        temporal = datos[n]
        izquierdo = 0
        derecho = n - 1
        while izquierdo <= derecho: #O(n)
            m = (izquierdo + derecho)//2
            if temporal <= datos[m]:
                derecho = m-1
            else:
                izquierdo = m + 1
            j = n - 1
        while j>=izquierdo: #O(n)
            datos[j+1] = datos[j]
            j-=1
        datos[izquierdo] = temporal
    return datos

def main():
    datos = [22,121,454,221,432,1,7,3,9]
    print(insertion_sort(datos))

if __name__ == '__main__':
    main()