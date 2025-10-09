# --- Implementación de una Cola sin objetos ---

# Cola vacía
cola = []

# --- Funciones básicas ---
def esta_vacia(cola):
    return len(cola) == 0  #len lee si la lista cola esta vacia con true 

def encolar(cola, elemento):  #Aqui con .append se agregan elementos a la cola
    cola.append(elemento)
    print(f"Se encoló: {elemento}") #se muestra cual

def desencolar(cola):  #Aqui se elimina el primer elemento de la cola con .pop
    if not esta_vacia(cola):
        elemento = cola.pop(0)
        print(f"Se desencoló: {elemento}") #muestra cual fue
        return elemento
    else:
        print("La cola está vacía. No se puede desencolar.") # o si no hay ninguno
        print()

def ver_frente(cola):  #Aqui te muestra cual es el elemente que esta hasta el frente 
    if not esta_vacia(cola):
        print(f"Elemento al frente: {cola[0]}") #cola[0] mostrando el primero
        return cola[0]
    else:
        print("La cola está vacía.")

def mostrar_cola(cola):
    print("Estado actual de la cola: ", cola) #imprime la cola completa


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