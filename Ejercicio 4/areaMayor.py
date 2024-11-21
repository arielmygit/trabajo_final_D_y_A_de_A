# calculamos el area mayor de un terreno triangular dado un conjunto de coordenadas

def obtenerTerrenos(coordenadas):
	coordenadasTriangulos =[]
	indice = 1
	tamaño = len(coordenadas)

	while indice < tamaño: #O(n²)
		if indice == (tamaño -1):
			break;
		indiceSecundario = indice
		indiceSecundario +=1
		for x in range(tamaño):
			#obtenemos las posibles combinaciones para formar n terrenos triangulares
			if indiceSecundario == tamaño:
				break
			coordenadasTriangulos.append(coordenadas[0])
			coordenadasTriangulos.append(coordenadas[indice])
			coordenadasTriangulos.append(coordenadas[indiceSecundario])
			indiceSecundario+=1
		indice +=1
	return coordenadasTriangulos

def obtenerAreas(terrenos):
	inicio = 0
	auxiliar = 0
	areas = []
	while inicio < len(terrenos):
		# calculamos el area en base a la siguiente formula: |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2
		if inicio > len(terrenos):
			break
		area = (terrenos[inicio][auxiliar]*(terrenos[inicio+1][auxiliar+1] - terrenos[inicio+2][auxiliar+1]) 
		  + terrenos[inicio + 1][auxiliar]*(terrenos[inicio+2][auxiliar+1] - terrenos[inicio][auxiliar+1]) 
		  + terrenos[inicio+2][auxiliar]*(terrenos[inicio][auxiliar+1] - terrenos[inicio+1][auxiliar+1]))
		if area < 0 :
			area *=-1 # si el area es negativo
		area /= 2
		areas.append(area)
		inicio +=3
	return areas

def obtenerMayor(areas,terrenos):
	mayor = max(areas)
	inicio = 0
	auxiliar = 0
	while inicio < len(terrenos): #O(log n)
		if inicio > len(terrenos): # O(1)
			break 
		area = (terrenos[inicio][auxiliar]*(terrenos[inicio+1][auxiliar+1] - terrenos[inicio+2][auxiliar+1]) 
		  + terrenos[inicio + 1][auxiliar]*(terrenos[inicio+2][auxiliar+1] - terrenos[inicio][auxiliar+1]) 
		  + terrenos[inicio+2][auxiliar]*(terrenos[inicio][auxiliar+1] - terrenos[inicio+1][auxiliar+1]))#O(1)
		if area < 0 : #O(1)
			area *=-1 # si el area es negativo
		area/= 2
		if area == mayor: #O(1)
			break
		inicio+=3 #O(1)

	print("Lar coordenadas del terreno con area mayor es: " + str(terrenos[inicio]) + str(terrenos[inicio+1]) + str(terrenos[inicio+2])) #O(1)
	print("Area: " + str(mayor)) #O(1)

def main():
	coordenadas = [[0,0],[4,0],[2,3],[1,1],[5,1],[3,4]]
	terrenos = obtenerTerrenos(coordenadas) #O(n²)
	areas = obtenerAreas(terrenos) # O(n)
	obtenerMayor(areas,terrenos) # O(n)
if __name__ == '__main__':
	main()