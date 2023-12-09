import random

def encontrar_posicion_vacia(matriz):
    posiciones_vacias = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                posiciones_vacias.append((i, j))
    return posiciones_vacias

def colocar_tres_cuatro(matriz):
    posiciones_vacias = encontrar_posicion_vacia(matriz)
    
    random.shuffle(posiciones_vacias)
    
    posicion_tres = None
    posicion_cuatro = None
    
    for pos in posiciones_vacias:
        i, j = pos
        if i > 0 and matriz[i - 1][j] != 4 and matriz[i - 1][j] != 7:
            posicion_tres = pos
            break
    
    for pos in posiciones_vacias:
        i, j = pos
        if i > 0 and matriz[i - 1][j] != 4 and matriz[i - 1][j] != 7 and pos != posicion_tres:
            posicion_cuatro = pos
            break
    
    if posicion_tres is not None and posicion_cuatro is not None:
        matriz[posicion_tres[0]][posicion_tres[1]] = 3
        matriz[posicion_cuatro[0]][posicion_cuatro[1]] = 2
    
    return matriz

def escribir_matriz_en_archivo(matriz, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for fila in matriz:
            fila_texto = ' '.join(map(str, fila)) + '\n'
            archivo.write(fila_texto)

matriz = [
    [4, 4, 0, 0, 0, 0, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 0, 0, 0, 0, 4, 4]
]

def ReiniciarMapa():
    escribir_matriz_en_archivo(matriz,"Prueba1.txt")