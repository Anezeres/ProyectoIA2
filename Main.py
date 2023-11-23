from Ventana import *
from Ventana2 import *
from Funciones import *

mapaTXT = "./Prueba1.txt"

with open(mapaTXT, "r") as archivo:
    mapa = []
    for linea in archivo:
        lista_de_numeros = [int(numero) for numero in linea.split()]
        mapa.append(lista_de_numeros)

    print("\n\nMAPA INICIAL\n")
    mostrarMapa(mapa)



    generarVentana(mapa)