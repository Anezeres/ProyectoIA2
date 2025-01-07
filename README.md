# Yoshi’s battle 
Es un juego entre dos adversarios en el que cada uno controla un Yoshi que
tiene los mismos movimientos de un caballo en el ajedrez. En las casillas del centro hay cuatro
monedas especiales, cada una otorga tres puntos a quien las tome primero. Las casillas cercanas
a las esquinas tienen monedas normales, cada una equivale a un punto. Después de que un Yoshi
tome una moneda (normal o especial), esa casilla no se puede volver a utilizar por ningún jugador.

![image](https://github.com/user-attachments/assets/acd1c35c-c70f-4bfe-9129-32f53390dadc)


El juego termina cuando no hayan más monedas. Gana el juego quien logre obtener más puntos
que su adversario. A continuación se muestra un posible estado inicial del juego.
Yoshi’s battle presenta tres niveles de dificultad (principiante, intermedio, y experto) que el
usuario puede seleccionar al iniciar el juego. Se debe construir un árbol minimax con decisiones
imperfectas. La profundidad límite del árbol depende del nivel seleccionado por el usuario. Para
el nivel principiante se utiliza un árbol de profundidad 2, para intermedio de profundidad 4, y
para experto de profundidad 6.
## Aclaraciones generales:
- El juego siempre lo inicia la máquina quien jugará con el Yoshi verde.
- Al empezar el juego, las monedas normales y especiales siempre aparecen en las posiciones
que se indican en la figura.
- Las posiciones iniciales de los Yoshis son aleatorias y no pueden coincidir con la ubicación de
las monedas.
- Se debe mostrar en cada momento del juego la cantidad de puntos de cada jugador.
- Al finalizar el juego se debe indicar quién es el ganador o si hubo empate.
Debe presentar un informe donde se defina y explique la función de utilidad heurística que se
utiliza en el algoritmo minimax.
