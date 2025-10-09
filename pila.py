# --- Implementación de una Pila sin objetos ---

# Pila vacía
pila = []

# --- Funciones básicas ---
def esta_vacia(pila):
    return len(pila) == 0

def apilar(pila, elemento):  # Push
    pila.append(elemento)
    print(f"Se apiló: {elemento}")

def desapilar(pila):  # Pop
    if not esta_vacia(pila):
        elemento = pila.pop()
        print(f"Se desapiló: {elemento}")
        return elemento
    else:
        print("La pila está vacía. No se puede desapilar.")

def ver_tope(pila):  # Peek
    if not esta_vacia(pila):
        print(f"Elemento en el tope: {pila[-1]}")
        return pila[-1]
    else:
        print("La pila está vacía.")

def mostrar_pila(pila):
    print("Estado actual de la pila:", pila)


# --- Uso paso a paso ---
print("¿La pila está vacía?", esta_vacia(pila))

apilar(pila, "Plato 1")
apilar(pila, "Plato 2")
apilar(pila, "Plato 3")

mostrar_pila(pila)
ver_tope(pila)

desapilar(pila)
mostrar_pila(pila)

desapilar(pila)
desapilar(pila)
desapilar(pila)  # Intento extra

print("¿La pila está vacía?", esta_vacia(pila))
