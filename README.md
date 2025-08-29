# Taller 1 Intr. Inteligencia Artificial

# Simulación de un Robot con Espacio de Estados y Sistema de Recompensa

Este proyecto implementa un modelo simplificado de un robot que se mueve en una cuadrícula 3x3, con un sistema de batería limitado, posibilidad de recarga y un objetivo en la posición (2,2). Se emplea un enfoque de espacio de estados para definir todas las configuraciones posibles del robot y se incluye un sistema de recompensas para evaluar su desempeño durante una simulación.

## 1. Estado inicial del robot

Se define el estado inicial como un diccionario con tres variables:

estado_robot = {
    "posicion": (0, 0),
    "bateria": 50,
    "objetivo_alcanzado": False
}

posicion → coordenadas (x,y) en la cuadrícula.
bateria → nivel de energía disponible (0 a 100).
objetivo_alcanzado → booleano que indica si el robot llegó al objetivo.


## 2. Espacio de estados

Se generan todas las combinaciones posibles de posición, batería y objetivo:

posiciones = [(x, y) for x in range(3) for y in range(3)]
baterias = [i for i in range(0, 101, 10)]
objetivos = [True, False]

espacio_estados = [(p, b, o) for p in posiciones for b in baterias for o in objetivos]

La cuadrícula tiene 9 posiciones posibles, la batería toma valores discretos de 0 a 100 en saltos de 10. El objetivo puede estar alcanzado o no y puede formar un espacio de estados finito y discreto.

## 3. Acciones posibles

El robot puede ejecutar las siguientes acciones:
acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]

Existen movimientos en 4 direcciones y recargar la batería que puede ser restaurada a 100.

## 4. Sistema de recompensas

Se define una función recompensa() que asigna valores en función de la acción y el estado resultante:

+30 → si llega al objetivo en ≤ 5 pasos.
+10 → si llega al objetivo en más de 5 pasos.
+5 → si recarga batería.
-1 → por cada movimiento (costo de energía).
-5 → si intenta moverse sin batería.

Esto incentiva al robot a llegar al objetivo rápido y administrar su energía.

## 5. Movimiento del robot

La función mover_robot() actualiza el estado según la acción elegida. Disminuye la batería en 10 unidades por movimiento, mantiene las posiciones dentro de la cuadrícula (0 a 2), recarga la batería si la acción es "recargar" y cambia objetivo_alcanzado = True si llega a (2,2).

## 6. Simulación

Se corre una simulación de 10 pasos aleatorios:

for paso in range(10):
    accion = random.choice(acciones)
    estado, no_bateria = mover_robot(estado, accion)
    r = recompensa(accion, estado, no_bateria, pasos)

En cada paso se elige una acción al azar, se actualiza el estado del robot, se calcula la recompensa obtenida. Al final se muestra la recompensa total acumulada.

En resumen, el script demuestra cómo con pocos elementos es posible modelar un agente autónomo que interactúa con su entorno, lo que abre la puerta a mejoras como políticas de decisión más inteligentes, algoritmos de optimización o integración con técnicas de machine learning.

