"""Desafio 1"""

import random
def crear_matriz(f,c):
    """
    pre: recibe f filas y c columnas
    pos: devuelve una matriz de FxC creada con ceros 
    """
    return [[0]*c for fil in range(f)]

def llenar_matriz(m):
    """
    pre: recibe una matriz ya creada
    pos: llena la matriz con valores (en este caso con random entre 1 y 10)
    """
    filas = len(m) #cant de listas dentro
    columnas = len(m[0]) #dentro de esa lista, longitud de esa lista
    for f in range(filas):
        for c in range(columnas):
            num = random.randint(1,10)
            m[f][c] = num

def imprimir_matriz(m,mats,estu):
    print(f"{'':15}",end="")
    for materia in mats:
        print(f"{materia:>15}",end="")
    print()

    # Imprimir las filas con los nombres de los estudiantes y sus calificaciones
    for i in range(len(estu)):
        print(f"{estu[i]:15}", end="")
        for j in range(len(mats)):
            print(f"{m[i][j]:15}", end="")
        print()

def promedio_estudiante(m,estu,mats):
    filas = len(m)
    columnas = len(m[0])
                            #sumas de notas por
    suma_filas = [0] * filas #estudiante
    suma_columnas = [0] * columnas #materia 
    # Calcula sumas totales por fila/columna
    for f in range(filas):
        for c in range(columnas):
            suma_filas[f] += m[f][c]
            suma_columnas[c] += m[f][c]
    
    # Calcula promedio de cada fila(estudiante) y cada columna(materia)
    print()
    for i in range(filas):
        prom_est = suma_filas[i] / columnas
        print("Promedio del estudiante",estu[i],"es de:",prom_est)

    print()
    
    for i in range(columnas):
        prom_mat = suma_columnas[i] / filas
        print("Promedio de Notas en",mats[i],"es de:",prom_mat)

#Programa Principal
estudiantes = ["Jorge Estefalo","Luis Rizzo","Juan Lopez","Maria Antonieta"]
materias = ["Matematica","Lengua","Quimica"]
matriz = crear_matriz(len(estudiantes),len(materias))
llenar_matriz(matriz)
imprimir_matriz(matriz,materias,estudiantes)
promedio_estudiante(matriz,estudiantes,materias)