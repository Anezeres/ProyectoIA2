import copy
import time
from Reader import Reader


def minimax(_matriz,pos,pos_ant,_recorrido,nivel):
    tiempo_inicio = time.time()
    caballo_jugador = 3
    espacio_vacio = 0
    x_fil,x_col = pos
    _matriz[x_fil][x_col] = caballo_jugador

    x_fil_ant,x_col_ant = pos_ant
    _matriz[x_fil_ant][x_col_ant] = espacio_vacio
    #Definicion de objetos del mapa
    casilla_tomada = 1
    
    moneda_uno = 4
    moneda_dos = 7   
    caballo_maquina = 2   
    
    puntos_moneda_uno = 1
    puntos_moneda_dos = 3
    profundidad_arbol = nivel


    matriz_inicial = _matriz
    matriz_original = copy.deepcopy(Reader('Prueba1.txt'))
    recorrido = [] 
    recorrido.extend(_recorrido)  
    recorrido_min = []
    cola = [{
        "matriz":matriz_inicial,
        "jugador": caballo_maquina,
        "rama_min_max": "max",
        "pocision_anterior": (0,0),
        "pocision_actual": (0,0),
        "puntos_obtenidos": 0,
        "beneficio_acumulado": 0,
        "profundidad": 0,
        "nodo_padre": 0, 
        "alpha": -10000000,
        "alpha_monedas": -10000000
    }]    
    nodos = []
    nodos.append(cola[0])

    
    def encontrar_posicion(matriz, numero):
        # Encuentra la posición actual del número en la matriz
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == numero:
                    return fila, columna
        return None   

    def sumatoria_beneficio(pocision, matriz):
        fila,columna = pocision
        movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
        suma = 0

        for mov in movimientos:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]

            if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]):
                if matriz[nueva_fila][nueva_columna] == 4 or matriz[nueva_fila][nueva_columna] == 7:
                    suma += matriz[nueva_fila][nueva_columna]

        return suma
    

    def movimiento_caballo(_cola, n, direccion):    

        matriz = _cola["matriz"]
        caballo_turno = _cola["jugador"]        
        posicion_actual = encontrar_posicion(matriz, caballo_turno)    
        rama_min_max = _cola["rama_min_max"]
        beneficio = _cola["beneficio_acumulado"]
        profundidad = _cola["profundidad"]        
        puntos_obtenidos = _cola["puntos_obtenidos"]
        alpha = _cola["alpha"]
        alpha_monedas = _cola["alpha_monedas"]
        

        if not posicion_actual:
            return matriz  # Si no se encuentra el número, no se realiza ningún movimiento
        fila, columna = posicion_actual
        # Definir los desplazamientos para las cuatro direcciones
        desplazamientos = {
            #desplazamiento en L atras
            "atras_arriba_dos": (-2, -1),
            "atras_arriba_una": (-1, -2),            
            "atras_abajo_una": (1, -2),
            "atras_abajo_dos": (2, -1),

            #desplazamiento en L adelante
            "adelante_abajo_dos": (2, 1),
            "adelante_abajo_una": (1, 2),            
            "adelante_arriba_una": (-1, 2),
            "adelante_arriba_dos": (-2, 1),
            
        }
        # Calcular la nueva posición
        desplazamiento = desplazamientos.get(direccion)    

        enemigo = caballo_maquina
        #Verificar cuál es el contrincante
        if(caballo_turno == caballo_maquina):
            enemigo = caballo_jugador        

        if desplazamiento:
            nueva_fila = fila + desplazamiento[0]
            nueva_columna = columna + desplazamiento[1]
            beneficio = sumatoria_beneficio((nueva_fila,nueva_columna),matriz) / 10

            if( 0 <= nueva_fila < len(matriz) and
                0 <= nueva_columna < len(matriz[nueva_fila]) and
                matriz[nueva_fila][nueva_columna] != enemigo 
                and matriz[nueva_fila][nueva_columna] != casilla_tomada
                ):

                #condicional en caso de que que caiga en una casilla vacía    
                if(matriz[nueva_fila][nueva_columna] == espacio_vacio):
                
                    matriz[fila][columna] = espacio_vacio
                    matriz[nueva_fila][nueva_columna] = caballo_turno               
                       
                    
                    cola.append({
                        "matriz":matriz,
                        "jugador": caballo_turno,
                        "rama_min_max": rama_min_max,
                        "pocision_anterior": (fila,columna),
                        "pocision_actual": (nueva_fila,nueva_columna),
                        "puntos_obtenidos": puntos_obtenidos,
                        "beneficio_acumulado": beneficio,
                        "profundidad": profundidad + 1, 
                        "nodo_padre": n
                    })
                    nodos.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos":0,
                            "puntos_acumulados": puntos_obtenidos,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n,
                            "alpha":alpha,
                            "alpha_monedas":alpha_monedas
                    })                   
                   
                    return        
                
                if(matriz[nueva_fila][nueva_columna] == moneda_uno):
                
                    matriz[fila][columna] = espacio_vacio
                    matriz[nueva_fila][nueva_columna] = caballo_turno               
                    cola.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos": puntos_obtenidos + puntos_moneda_uno,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n
                        })
                    nodos.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos": puntos_moneda_uno,
                            "puntos_acumulados": puntos_obtenidos + puntos_moneda_uno,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n,
                            "alpha":alpha,
                            "alpha_monedas":alpha_monedas
                    })
                    return
                
                #Condicional para movimiento en casilla con moneda 

                if(matriz[nueva_fila][nueva_columna] == moneda_dos):
                
                    matriz[fila][columna] = espacio_vacio
                    matriz[nueva_fila][nueva_columna] = caballo_turno               
                    cola.append({
                        "matriz":matriz,
                        "jugador": caballo_turno,
                        "rama_min_max": rama_min_max,
                        "pocision_anterior": (fila,columna),
                        "pocision_actual": (nueva_fila,nueva_columna),
                        "puntos_obtenidos": puntos_obtenidos + puntos_moneda_dos,
                        "beneficio_acumulado": beneficio,
                        "profundidad": profundidad + 1, 
                        "nodo_padre": n
                    })
                    nodos.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos":puntos_moneda_dos,
                            "puntos_acumulados": puntos_obtenidos + puntos_moneda_dos,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n,
                            "alpha":alpha,
                            "alpha_monedas":alpha_monedas 
                    })
                return                
            return
        return 
    
    estado_jugador = [
        {
                        
                        "pocision_anterior": (0,0),
                        "pocision_actual": (0,0),                        
                        "puntos_acumulados": 0                        
        }
    ]
    
    def movimiento_caballo_jugador(anterior,nuevo):      

        fila,columna = anterior
        nueva_fila,nueva_columna = nuevo
        caballo_turno = caballo_jugador
        matriz = _matriz        
        enemigo = caballo_maquina  

        if( 0 <= nueva_fila < len(matriz) and
            0 <= nueva_columna < len(matriz[nueva_fila]) and
            matriz[nueva_fila][nueva_columna] != enemigo 
            and matriz[nueva_fila][nueva_columna] != casilla_tomada
            ):

            #condicional en caso de que que caiga en una casilla vacía    
            if(matriz[nueva_fila][nueva_columna] == espacio_vacio):
            
                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               

                estado_jugador[0]["pocision_anterior"] = (fila,columna)
                estado_jugador[0]["pocision_actual"] = (nueva_fila,nueva_columna)                       
                estado_jugador[0]["puntos_acumulados"] =  estado_jugador[0]["puntos_acumulados"]                              
                
                return        
            
            if(matriz[nueva_fila][nueva_columna] == moneda_uno):
            
                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               

                estado_jugador[0]["pocision_anterior"] = (fila,columna)
                estado_jugador[0]["pocision_actual"] = (nueva_fila,nueva_columna)                       
                estado_jugador[0]["puntos_acumulados"] =  estado_jugador[0]["puntos_acumulados"]  + puntos_moneda_uno       
               
                return
            
            #Condicional para movimiento en casilla con moneda 

            if(matriz[nueva_fila][nueva_columna] == moneda_dos):
            
                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               

                estado_jugador[0]["pocision_anterior"] = (fila,columna)
                estado_jugador[0]["pocision_actual"] = (nueva_fila,nueva_columna)                       
                estado_jugador[0]["puntos_acumulados"] =  estado_jugador[0]["puntos_acumulados"]  + puntos_moneda_dos   
                return                
            return
        return

    def distancia_manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def encontrar_posicion_mas_cercana(matriz, fila, columna):
        uno_o_dos_encontrado = False
        distancia_mas_cercana = float('inf')
        posicion_mas_cercana = None

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == 4 or matriz[i][j] == 7:
                    uno_o_dos_encontrado = True
                    dist = distancia_manhattan((fila, columna), (i, j))
                    if dist < distancia_mas_cercana:
                        distancia_mas_cercana = dist
                        posicion_mas_cercana = (i, j)

        return uno_o_dos_encontrado, posicion_mas_cercana

    def encontrar_mejor_movimiento_en_L(matriz, fila, columna, fila_previa, columna_previa, visitados):
        movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
        uno_o_dos_cercano, posicion_mas_cercana = encontrar_posicion_mas_cercana(matriz, fila, columna)

        if not uno_o_dos_cercano:
            return None

        mejor_movimiento = None
        mejor_distancia = float('inf')

        for mov in movimientos:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]

            if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]) and (nueva_fila, nueva_columna) != (fila_previa, columna_previa) and (nueva_fila, nueva_columna) not in visitados and  matriz[nueva_fila][nueva_columna] != casilla_tomada and matriz[nueva_fila][nueva_columna] != caballo_jugador:
                dist = distancia_manhattan((nueva_fila, nueva_columna), posicion_mas_cercana)
                if dist < mejor_distancia:
                    mejor_distancia = dist
                    mejor_movimiento = (nueva_fila, nueva_columna)

        return mejor_movimiento

    def encontrar_camino_hacia_1_o_2(matriz, fila_inicial, columna_inicial, posiciones_evitar):
        visitados = set(posiciones_evitar)
        camino = [(fila_inicial, columna_inicial)]

        fila_previa = None
        columna_previa = None

        while True:
            movimiento = encontrar_mejor_movimiento_en_L(matriz, camino[-1][0], camino[-1][1], fila_previa, columna_previa, visitados)
            if movimiento is None:
                break
            visitados.add(movimiento)
            camino.append(movimiento)
            fila_previa, columna_previa = camino[-2]

            if matriz[movimiento[0]][movimiento[1]] == 4 or matriz[movimiento[0]][movimiento[1]] == 7:
                break

        return camino        

    def mover_caballo():        
        n = 0
        profundidad = 0
        caballo_turno = caballo_maquina
        rama_min_max = "max"
        while True:        
            m = cola[0]        
            if (profundidad < m["profundidad"]):
                profundidad = m["profundidad"]
                if m["jugador"] == caballo_maquina:
                    caballo_turno = caballo_jugador
                    rama_min_max = "min"                    
                elif m["jugador"] == caballo_jugador:
                    caballo_turno = caballo_maquina    
                    rama_min_max = "max"                   
                
            if  rama_min_max == 'min':
                m["alpha"] = -10000000    
                m["alpha_monedas"] = -10000000 
            elif rama_min_max == 'max':
                m["alpha"] = -10000000    
                m["alpha_monedas"] = -10000000             
            
            m["jugador"] = caballo_turno
            m["rama_min_max"] = rama_min_max
            if m["profundidad"]  == profundidad_arbol:
                break

            
            # ADELANTE 

            #movimiento en L atras arriba dos casillas
            mov_atras_arriba_dos = movimiento_caballo(copy.deepcopy(m),n, "atras_arriba_dos")

            #movimiento en L atras arriba una casilla
            mov_atras_arriba_uno = movimiento_caballo(copy.deepcopy(m), n, "atras_arriba_una")               

            #movimiento en L atras arriba dos casillas
            mov_atras_abajo_uno = movimiento_caballo(copy.deepcopy(m),n, "atras_abajo_una")

            #movimiento en L atras arriba dos casillas
            mov_atras_abajo_dos = movimiento_caballo(copy.deepcopy(m),n, "atras_abajo_dos")

            
            #ADELANTE

            #movimiento en L atras arriba dos casillas
            mov_adelante_abajo_dos = movimiento_caballo(copy.deepcopy(m),n, "adelante_abajo_dos")  


            #movimiento en L atras arriba dos casillas
            mov_adelante_abajo_una = movimiento_caballo(copy.deepcopy(m),n, "adelante_abajo_una")
            

            #movimiento en L atras arriba una casilla
            mov__adelante_arriba_una = movimiento_caballo(copy.deepcopy(m),n, "adelante_arriba_una")            

            #movimiento en L atras arriba dos casillas
            mov__adelante_arriba_dos = movimiento_caballo(copy.deepcopy(m),n, "adelante_arriba_dos")
            
            cola.pop(0)              
            n += 1           
        
        
        j = profundidad_arbol
        i = 0
            
        while j >= 0:   

            if nodos[i]["profundidad"] == profundidad:                 
                if nodos[i]["rama_min_max"] == "min": 
                    if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                        if nodos[i]["puntos_obtenidos"] <  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (-1 * nodos[i]["puntos_obtenidos"]) / 10                            
                            

                    elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                        if (nodos[i]["beneficio_acumulado"] < nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (-1 * nodos[i]["beneficio_acumulado"])                             
                            
                            
                    elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):     
                        if (nodos[nodos[i]["nodo_padre"]]["alpha"] < 0): 
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = 0     
                elif nodos[i]["rama_min_max"] == "max": 
                    if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                        if nodos[i]["puntos_obtenidos"] >  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (-1 * nodos[i]["puntos_obtenidos"]) / 10                            
                            

                    elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                        if (nodos[i]["beneficio_acumulado"] > nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (-1 * nodos[i]["beneficio_acumulado"])                             
                            
                            
                    elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):     
                        if (nodos[nodos[i]["nodo_padre"]]["alpha"] < 0): 
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = 0            

            elif nodos[i]["profundidad"] == 1:                 
                if nodos[i]["rama_min_max"] == "max": 
                    if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                        if nodos[i]["puntos_obtenidos"] >  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (nodos[i]["puntos_obtenidos"] + nodos[i]["alpha"])                          
                            nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                            nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                            

                    elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                        if (nodos[i]["beneficio_acumulado"] > nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (nodos[i]["beneficio_acumulado"] + nodos[i]["alpha"])                             
                            nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                            nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                            #recorrido.clear()
                            
                    elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):     
                        if (nodos[nodos[i]["nodo_padre"]]["alpha"] <= 0): 
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = 0    
                            # nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = encontrar_posicion(_matriz,caballo_maquina) 
                            # fil,col = nodos[nodos[i]["nodo_padre"]]["pocision_anterior"]
                            # pos_act = encontrar_camino_hacia_1_o_2(_matriz,fil,col,recorrido)    
                            # recorrido.append(pos_act[0])        
                                                
                            # nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = pos_act[1]
                         

            elif nodos[i]["profundidad"] < profundidad:                 
                if nodos[i]["rama_min_max"] == "min": 
                    if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                        if nodos[i]["puntos_obtenidos"] <  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (nodos[i]["alpha"] + ((-1 * nodos[i]["puntos_obtenidos"]) / 10))           
                            

                    elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                        if (nodos[i]["beneficio_acumulado"] < nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = (nodos[i]["alpha"] + (-1 * nodos[i]["beneficio_acumulado"]))                             
                            
                            
                    elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):     
                        if (nodos[nodos[i]["nodo_padre"]]["alpha"] < 0): 
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = 0     

                elif nodos[i]["rama_min_max"] == "max": 
                    if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                        if nodos[i]["puntos_obtenidos"] >  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["puntos_obtenidos"] + nodos[i]["alpha"]                   
                            

                    elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                        if (nodos[i]["beneficio_acumulado"] > nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                            nodos[nodos[i]["nodo_padre"]]["alpha"] =  nodos[i]["beneficio_acumulado"] + nodos[i]["alpha"]                           
                            
                            
                    elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):     
                        if (nodos[nodos[i]["nodo_padre"]]["alpha"] < 0): 
                            nodos[nodos[i]["nodo_padre"]]["alpha"] = 0            
            
            i += 1     
            if i == len(nodos):
                j -= 1    
                i = 0        

        if nodos[0]["alpha"] >= 1:
           recorrido.clear()
           print("recorrido menor")
        elif nodos[0]["alpha"] < 1:
            nodos[0]["pocision_anterior"] = encontrar_posicion(_matriz,caballo_maquina) 
            fil,col = nodos[0]["pocision_anterior"]
            pos_act = encontrar_camino_hacia_1_o_2(_matriz,fil,col,recorrido)              
            recorrido.append(pos_act[0])  
            nodos[0]["pocision_actual"] = pos_act[1]                       
                  
        fila_anterior, columna_anterior = nodos[0]["pocision_anterior"]
        fila_actual, columna_actual = nodos[0]["pocision_actual"]
    
        _matriz[fila_anterior][columna_anterior] = espacio_vacio
        _matriz[fila_actual][columna_actual] = caballo_maquina    
        
        print(nodos[0]["alpha"])
        
        comparar_matrices(matriz_original,_matriz)
        imprimir_matriz(_matriz) 
        #print(recorrido)
        # fila_anterior_jugador,columna_anterior_jugador = encontrar_posicion(_matriz, caballo_jugador)    
        # fila_jugador = int(input("Ingrese la posición de la fila: "))
        # columna_jugador = int(input("Ingrese la posición de la columna: "))
        # movimiento_caballo_jugador(( fila_anterior_jugador,columna_anterior_jugador),(fila_jugador,columna_jugador))
        comparar_matrices(matriz_original,_matriz)
        

    def imprimir_matriz(matriz):
        for fila in matriz:
            print(" ".join(map(str, fila)))

    def comparar_matrices(matriz_modelo, segunda_matriz):
        for i in range(len(matriz_modelo)):
            for j in range(len(matriz_modelo[0])):
                if matriz_modelo[i][j] in [4] and segunda_matriz[i][j] == 0:
                    segunda_matriz[i][j] = 1            
    mover_caballo() 
    comparar_matrices(matriz_original,_matriz)
    #imprimir_matriz(_matriz)  
    # while True:
    #     comparar_matrices(matriz_original,_matriz) 
    #     mover_caballo()         
                 
    #     cola = [{
    #         "matriz":matriz_inicial,
    #         "jugador": caballo_maquina,
    #         "rama_min_max": "max",
    #         "pocision_anterior": (0,0),
    #         "pocision_actual": (0,0),
    #         "puntos_obtenidos": 0,
    #         "beneficio_acumulado": 0,
    #         "profundidad": 0,
    #         "nodo_padre": 0, 
    #         "alpha": -10000000,
    #         "alpha_monedas": -10000000
    #     }]
        
    #     #nodos = []
    #     nodos.append(cola[0])         
    #     print(estado_jugador)
    comparar_matrices(matriz_original,_matriz)
    estado = {
        "matriz" :_matriz,
        "recorrido": recorrido
    }
   
    return estado


array = []
#minimax(Reader('Prueba1.txt'),(2,5),(3,7),array)
#print(Reader('Prueba1.txt'))
#print(agente_amplitud(Reader('Prueba1.txt')))