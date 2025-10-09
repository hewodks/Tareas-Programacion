# --- Implementación de una Cola sin objetos ---

# Cola vacía
cola = []

# --- Funciones básicas ---
def esta_vacia(cola):
    return len(cola) == 0  #len 

def encolar(cola, elemento):  # Enqueue
    cola.append(elemento)
    print(f"Se encoló: {elemento}")

def desencolar(cola):  # Dequeue
    if not esta_vacia(cola):
        elemento = cola.pop(0)
        print(f"Se desencoló: {elemento}")
        return elemento
    else:
        print("La cola está vacía. No se puede desencolar.")

def ver_frente(cola):  # Front
    if not esta_vacia(cola):
        print(f"Elemento al frente: {cola[0]}")
        return cola[0]
    else:
        print("La cola está vacía.")

def mostrar_cola(cola):
    print("Estado actual de la cola:", cola)


# --- Uso paso a paso ---
print("¿La cola está vacía?", esta_vacia(cola))

encolar(cola, "Persona 1")
encolar(cola, "Persona 2")
encolar(cola, "Persona 3")

mostrar_cola(cola)
ver_frente(cola)

desencolar(cola)
mostrar_cola(cola)

desencolar(cola)
desencolar(cola)
desencolar(cola)  # Intento extra

print("¿La cola está vacía?", esta_vacia(cola))