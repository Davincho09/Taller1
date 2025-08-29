import random

estado_robot = {
    "posicion": (0, 0),
    "bateria": 50,
    "objetivo_alcanzado": False
}

print("Estado inicial del robot:", estado_robot)

# Predicción actualizada con el espacio de estados
posiciones = [(x, y) for x in range(3) for y in range(3)]
baterias = [i for i in range(0, 101, 10)] 
objetivos = [True, False]

espacio_estados = [(p, b, o) for p in posiciones for b in baterias for o in objetivos]
print("Movimientos posibles:", len(espacio_estados))

acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]
print("\nAcciones posibles:", acciones)


# Sistema de recompensa
def recompensa(accion, nuevo_estado, no_bateria, pasos):
    if accion == "recargar":
        return 5
    elif nuevo_estado["objetivo_alcanzado"]:
        if pasos <= 5:
            return 30  # Bonus por pocos pasos
        else:
            return 10
    elif no_bateria:
        return -5  # Costo de moverse sin batería
    elif accion in ["adelante", "atras", "izquierda", "derecha"]:
        return -1  # Costo de moverse
    else:
        return 0


# Movimiento del robot
def mover_robot(estado, accion):
    no_bateria = False
    x, y = estado["posicion"]

    if accion in ["adelante", "atras", "izquierda", "derecha"]:
        if estado["bateria"] <= 0:
            no_bateria = True
            return estado, no_bateria
        else:
            estado["bateria"] -= 10  # Energía gastada al moverse

    if accion == "adelante":
        x = min(x + 1, 2)
    elif accion == "atras":
        x = max(x - 1, 0)
    elif accion == "derecha":
        y = min(y + 1, 2)
    elif accion == "izquierda":
        y = max(y - 1, 0)
    elif accion == "recargar":
        estado["bateria"] = 100

    estado["posicion"] = (x, y)

    # El objetivo se alcanzó?
    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    return estado, no_bateria


# Simulación
estado = {"posicion": (0, 0), "bateria": 50, "objetivo_alcanzado": False}
recompensa_total = 0
pasos = 0

for paso in range(10):
    pasos += 1
    accion = random.choice(acciones)
    estado, no_bateria = mover_robot(estado, accion)
    r = recompensa(accion, estado, no_bateria, pasos)
    recompensa_total += r

    print(f"Paso {paso+1}: Acción = {accion}, Estado = {estado}, Recompensa = {r}")

print("\nRecompensa total obtenida:", recompensa_total)
