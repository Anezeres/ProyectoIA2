#from Config import route
from tkinter import filedialog

def Reader(nombre_archivo):
    numero_agente = 5
    def leer_matriz(nombre_archivo):
        matriz = []
        try:
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    fila = [int(valor) for valor in linea.strip().split()]
                    matriz.append(fila)
            return matriz
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no se encuentra.")
            return None
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {str(e)}")
            return None

    # Nombre del archivo que contiene la matriz
  

    # Llama a la función para leer y almacenar la matriz
    matriz = leer_matriz(nombre_archivo)
    
    #def get_matriz():
          

    def posicion_agente():
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == numero_agente:
                    return fila, columna
        # Si no se encuentra el agente en la matriz, retorna nada
        return None
    return matriz

# agente = posicion_agente()


