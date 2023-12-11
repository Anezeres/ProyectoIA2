import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import filedialog
from minimax import minimax

global ventana
global yoshiBueno
global gema
global lienzo
global mapa
global listaMovimientos
global listaObjetos
global boton1, boton2, botonVolver
global boton3, boton4, boton5, iniciarJuegoBtn

global posYoshiBueno, posYoshiEnemigo
global juegoIniciado
global recorrido
global nivel
global puntos_jugador
global puntos_maquina
global label_jugador
global label_jugador_2

puntos_jugador = 0
puntos_maquina = 0



filaCursorActual=0
columnaCursorActual = 0

juegoIniciado = False
listaObjetos = []
recorrido = []

def generarVentana(mapaRecibido):
    global lienzo
    global ventana
    global mapa
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, iniciarJuegoBtn
    global recorrido
    global puntos_jugador
    global puntos_maquina
    global label_jugador
    global label_jugador_2

    #TODO Ahora hay que hacer que cuando le de click al boton el soldado empiece a moverse por el mapa

    #recorrido = []
    mapa = mapaRecibido
    ventana = tk.Tk()
    ventana.title("Mostrar Primer Sprite")
    botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("Volver"))
    boton1 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton1"))
    boton2 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton2"))
    boton3 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton3"))
    boton4 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton4"))
    boton5 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton5"))
    iniciarJuegoBtn = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("iniciarJuegoBtn"))
    

    frame_labels = tk.Frame(ventana)
    #frame_labels.pack()
    frame_labels.pack(side=tk.BOTTOM, pady=10)

    # Creamos los labels para Jugador 1 y Jugador 2 dentro del contenedor
    label_jugador = tk.Label(frame_labels, text="Puntos Jugador: " + str(puntos_jugador), fg="blue")
    label_jugador.pack(side=tk.LEFT, padx=10)  # Alineamos a la izquierda con un pequeño espacio a la derecha

    label_jugador_2 = tk.Label(frame_labels, text="Puntos Máquina: "+ str(puntos_maquina), fg="red")
    label_jugador_2.pack(side=tk.LEFT, padx=10)

    

    lienzo = tk.Canvas(ventana, width=640, height=510)
    
    lienzo.pack()
    #lienzo.lift(frame_labels)

    

    ventanaIniciarJuego()
    #ventana.bind("<Motion>", imprimirCordenada)
    ventana.bind("<Button-1>", imprimirCordenada)
    
    
    ventana.geometry("512x550")
    ventana.mainloop()


def ventanaIniciarJuego():

    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, iniciarJuegoBtn

    destruirBotones()

    iniciarJuegoBtn = tk.Button(ventana, text="Iniciar",width=19,height=1, command=lambda: seleccionarDificultad())
    iniciarJuegoBtn.place(x=22, y=445)

    agregarImagenMenu("InicioJuego")

def seleccionarDificultad():

    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5

    destruirBotones()

    boton3 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientosAmplitud())
    boton3.place(x=22, y=173)

    boton4 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: nivel_intermedio())
    boton4.place(x=22, y=270)

    boton5 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: nivel_avanzado())
    boton5.place(x=22, y=364)

    """ botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mostrarOpcionesIniciales())
    botonVolver.place(x=47, y=600) """

    """ agregarImagenMenu("NoInformadaOpciones") """


    agregarImagenMenu("Dificultad")

def abrirArchivos():
    global mapa

    archivo = filedialog.askopenfilename()

    if archivo:
        print(f"Archivo seleccionado: {archivo}")

        try:
            mapa = []
            with open(archivo, 'r') as file:
                for linea in file:
                    lista_de_numeros = [int(numero) for numero in linea.split()]
                    mapa.append(lista_de_numeros)

            print("\n\nMAPA SECUNDARIA\n")
            """ mostrarMapa(mapa) """

            """ mostrarOpcionesIniciales() """
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
    else:
        print("Ningún archivo seleccionado.")


    
    return 0

def crearSprite(x,y):
        # Coordenadas del área a recortar
    imagen = Image.open("Sprites/sprites.png")
    x_inicio = x * 16
    y_inicio = y * 16
    ancho_recorte =16
    alto_recorte = 16



    # Recortar la imagen
    imagen_recortada = imagen.crop((x_inicio, y_inicio, x_inicio + ancho_recorte, y_inicio + alto_recorte))

    # Convertir la imagen recortada a PhotoImage para Tkinter
    imagen_escala = imagen_recortada.resize((64, 64), Image.ADAPTIVE)
    imagen_tk = ImageTk.PhotoImage(imagen_escala)

    # Crear una etiqueta para mostrar la imagen
    return imagen_tk

def dibujarSprites(imagen):
    global yoshiBueno
    global lienzo
    global mapa
    global posYoshiBueno
    global gema
    global puntos_jugador

    x = 0
    y = 0
    filas = 8
    columnas = 8
    sprite_size = 64
    
    
    

    for fila in range(filas):
        for columna in range(columnas):
            posX = x + columna * sprite_size
            posY = y + fila * sprite_size

            lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[0])

            if(mapa[fila][columna] == 1):
                piedra = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[1])
                lienzo.lift(piedra)
            elif(mapa[fila][columna] == 2):
                yoshiEnemigo = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[2])
                lienzo.lift(yoshiEnemigo)
                agregarObjetoLista(fila,columna,yoshiEnemigo)
            elif(mapa[fila][columna] == 3):
                posYoshiBueno = (fila,columna)
               # print("Dibjado de Yoshi: ", posX,posY)
                yoshiBueno = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[3])
                lienzo.lift(yoshiBueno)
            elif(mapa[fila][columna] == 4):
                coin = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[4])
                lienzo.lift(coin)
                agregarObjetoLista(fila,columna,coin)
            elif(mapa[fila][columna] == 7):
                coinSuper = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[7])
                lienzo.lift(coinSuper)
                agregarObjetoLista(fila,columna,coinSuper)           
                 

def dibujarCursor(fila, columna, imagen):
    global lienzo
    global mapa
    global gema

    x = 0
    y = 0
    sprite_size = 64

    posX = x + columna * sprite_size
    posY = y + fila * sprite_size
    
    if(esMovimientoPosible((fila, columna))):       
        moverYoshi(posX, posY,(fila,columna))        
        print("Se puede mover aquí")

    else:
        #lienzo.itemconfig(gema, image=imagen[6])
        #moverGema(posX, posY)
        print("No se puede mover aquí")


def agregarObjetoLista(fila,columna,objeto):
    global listaObjetos

    listaObjetos.append([fila,columna,objeto])

def crearSprites():
    global sprites

    coinPng = Image.open("Sprites/Coin.png")
    coinSuperPng = Image.open("Sprites/CoinSuper.png")
    yoshiEnemigoPng = Image.open("Sprites/Rojo.png")
    yoshiBuenoPng = Image.open("Sprites/Azul.png")

    gemaVerdePng = Image.open("Sprites/pastoAzul.jpg")
    gemaVerdePng = gemaVerdePng.resize((64, 64), Image.ADAPTIVE)
    gemaRojaPng = Image.open("Sprites/GemaRoja.png")


    yoshiBuenoGrande = yoshiBuenoPng.resize((64,64), Image.ADAPTIVE)
    yoshiEnemigoGrande = yoshiEnemigoPng.resize((64,64), Image.ADAPTIVE)
    coinGrande = coinPng.resize((64,64), Image.ADAPTIVE)
    coinSuperGrande = coinSuperPng.resize((64,64), Image.ADAPTIVE)

    sprites = []

    imagen_p = Image.open("Sprites/pasto.jpg")
    imagen_escala_p = imagen_p.resize((64, 64), Image.ADAPTIVE)
    imagenPasto = ImageTk.PhotoImage(imagen_escala_p )

    # imagenPasto = crearSprite(19,8)
    imagenPiedra = crearSprite(17,10)
    
    yoshiEnemigo = ImageTk.PhotoImage(yoshiEnemigoGrande)
    yoshiBueno = ImageTk.PhotoImage(yoshiBuenoGrande)
    coin = ImageTk.PhotoImage(coinGrande)
    coinSuper = ImageTk.PhotoImage(coinSuperGrande)

    gemaVerde = ImageTk.PhotoImage(gemaVerdePng)
    gemaRoja = ImageTk.PhotoImage(gemaRojaPng)

    sprites.append(imagenPasto)
    sprites.append(imagenPiedra)
    sprites.append(yoshiEnemigo)
    sprites.append(yoshiBueno)
    sprites.append(coin)
    sprites.append(gemaVerde)
    sprites.append(gemaRoja)
    sprites.append(coinSuper)

    return sprites 

def moverGema(xNueva, yNueva):
    global lienzo
    global gema
    global yoshiBueno
    global ventana
    global label_jugador
    
    lienzo.lift(gema)

    lienzo.coords(gema, xNueva, yNueva)

    ventana.update()

    return 0

def moverYoshi(xNueva, yNueva,pos):
    global lienzo
    global gema
    global yoshiBueno
    global ventana
    global mapa
    global posYoshiBueno
    global recorrido
    global nivel
    global puntos_maquina
    global puntos_jugador
    global label_jugador
    global label_jugador_2
    
    
    imprimir_matriz(mapa)   
    response = minimax(mapa,pos,posYoshiBueno,recorrido,nivel,puntos_maquina,puntos_jugador)    
    if response["juego_terminado"] :
        print("GAME OVER")
    mapa = response["matriz"]    
    recorrido = response["recorrido"]  
    # Variables que cuentan los puntos
    puntos_jugador = response["puntos_jugador"]
    puntos_maquina = response["puntos_maquina"]  
    print("PUNTOS JUGADOR", puntos_jugador)
    print("PUNTOS MAQUINA", puntos_maquina)

    lienzo.lift(yoshiBueno)      
    lienzo.coords(yoshiBueno, xNueva, yNueva)
    lista_sprites = crearSprites()
    dibujarSprites(lista_sprites)    
    if response["juego_terminado"] :
        if puntos_jugador > puntos_maquina:
            label_jugador.config(text="EL JUGADOR HA GANADO: " + str(puntos_jugador) + " - "+ str(puntos_maquina))
            label_jugador_2.config(text="")   
        elif puntos_jugador < puntos_maquina:
            label_jugador.config(text="" )
            label_jugador_2.config(text="LA MAQUINA HA GANADO: " + str(puntos_maquina) + " - "+ str(puntos_jugador))  
        elif   puntos_jugador == puntos_maquina :
            label_jugador.config(text="EMPATE " )
            label_jugador_2.config(text="EMPATE: " + str(puntos_jugador) + " - "+ str(puntos_maquina)) 
    elif not response["juego_terminado"] :            
        label_jugador.config(text="Puntos Jugador: " + str(puntos_jugador))
        label_jugador_2.config(text="Puntos Máquina: " + str(puntos_maquina))
    ventana.update()

    return 0
def imprimir_matriz(matriz):
        for fila in matriz:
            print(" ".join(map(str, fila)))    
def identificarMovimientosCompletos():
    global listaMovimientos

    for lista_de_movimientos in listaMovimientos:

        for i in range(1, len(lista_de_movimientos)):
            fila_anterior, columna_anterior = lista_de_movimientos[i - 1]
            fila_actual, columna_actual = lista_de_movimientos[i]

            # Comparamos las filas y columnas para determinar la dirección
            if fila_anterior < fila_actual:
                direccion = "Abajo"
            elif fila_anterior > fila_actual:
                direccion = "Arriba"
            elif columna_anterior < columna_actual:
                direccion = "Derecha"
            elif columna_anterior > columna_actual:
                direccion = "Izquierda"

            
            #moverSoldado(0, direccion)
            eliminarObjeto(fila_actual, columna_actual)
            time.sleep(1)

def generarMovimientosAmplitud():
    global listaMovimientos
    global lienzo
    global juegoIniciado
    global nivel
    nivel = 2


    juegoIniciado = True
    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)

    variables = input("Pido el Input: \n")

    """ cicloBombero(mapa)
    listaMovimientos = getListaMovimientos()
    print("Lista movimientos: ", listaMovimientos)
    identificarMovimientosCompletos()
    ventanaIniciarJuego() """


def nivel_intermedio():
    global listaMovimientos
    global lienzo
    global juegoIniciado
    global nivel
    nivel = 4


    juegoIniciado = True
    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)

    variables = input("Pido el Input: \n")

def nivel_avanzado():
    global listaMovimientos
    global lienzo
    global juegoIniciado
    global nivel
    nivel = 6


    juegoIniciado = True
    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)

    variables = input("Pido el Input: \n")

def eliminarObjeto(fila, columna):
    global listaObjetos
    global lienzo

    for sublista in listaObjetos:
        if sublista[0] == fila and sublista[1] == columna:
            lienzo.delete(sublista[2])






def mostrarOpcionesNoInformada():
    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5

    destruirBotones()

    boton3 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientosAmplitud())
    boton3.place(x=47, y=160)

    boton4 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: nivel_intermedio())
    boton4.place(x=47, y=327)

    boton5 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda:nivel_avanzado())
    boton5.place(x=47, y=497)

    botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mostrarOpcionesIniciales())
    botonVolver.place(x=47, y=600)

    agregarImagenMenu("NoInformadaOpciones")

def mostrarOpcionesInformada():
    
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5

    destruirBotones()

    boton1 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: mensaje("Avara"))
    boton1.place(x=46, y=220)

    boton2 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: mensaje("A*"))
    boton2.place(x=46, y=388)

    botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("Volver"))
    botonVolver.place(x=47, y=600)

    agregarImagenMenu("InformadaOpciones")
    
    

def agregarImagenMenu(Imagen):
    global lienzo, OpcionesImg
    opciones = Image.open(f"Intro/{Imagen}.png")
    OpcionesImg = ImageTk.PhotoImage(opciones)
    imagen = lienzo.create_image(0,0, anchor=tk.NW, image=OpcionesImg)
    lienzo.lift(imagen)


def destruirBotones():
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, iniciarJuegoBtn
    
    boton1.destroy()
    boton2.destroy()
    boton3.destroy()
    boton4.destroy()
    boton5.destroy()
    iniciarJuegoBtn.destroy()
    botonVolver.destroy()


def mensaje(mensaje):
    print("Mensaje: ", mensaje)


def imprimirCordenada(event):
    global juegoIniciado
    global sprites
    
    

    x = ventana.winfo_pointerx() - ventana.winfo_rootx()
    y = ventana.winfo_pointery() - ventana.winfo_rooty()


    fila = int((y / 512) * 8) 
    columna = int((x / 512) * 8) 
    print(f"Celda: ({fila}, {columna})")

    if(juegoIniciado):
        """ sprites = crearSprites() """
        dibujarCursor(fila, columna, sprites)

    return fila,columna


def esMovimientoPosible(posCursos):
    global posYoshiBueno
    global mapa
    print("Cordenada: ", posCursos)
    # Definir todos los posibles movimientos en L
    movimientosEnL = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    
    print("POSSS CURSORR")
    fil_cur,col_cur = posCursos
    if mapa[fil_cur][col_cur] == 1:
        return False
    if mapa[fil_cur][col_cur] == 2:
        return False
    #print(mapa[fil_cur][col_cur])
    # Verificar si la posición de verificación está en un movimiento en L
    for movimiento in movimientosEnL:
        nueva_pos = (posYoshiBueno[0] + movimiento[0], posYoshiBueno[1] + movimiento[1])
        if nueva_pos == posCursos:
            return True
        
    
    # Si no se encuentra ninguna coincidencia, no es un movimiento en L válido
    return False