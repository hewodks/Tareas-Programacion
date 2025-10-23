import re
import getpass
import time

# --- Constantes y Variables Globales ---
# Lista de contraseñas débiles (Al menos 5) [cite: 19]
WEAK_PASSWORDS = ["123", "password", "123456", "qwerty", "abc123", "login", "admin", "iloveyou"]
# Historial guarda: (contraseña, puntaje, es_segura) [cite: 39]
password_history = []
secure_count = 0 # Contraseñas seguras [cite: 40, 47]
weak_count = 0   # Contraseñas débiles [cite: 40, 46]

# --- Funciones de Utilidad ---

def welcome_message():
    """Pide el nombre del usuario y muestra un mensaje de bienvenida tipo hacker. """
    print("\n" + "="*50)
    print("      <<< LABORATORIO DE CONTRASEÑAS HACKER EDITION >>>")
    print("="*50)
    user_name = input("INICIE SESIÓN -- Ingrese su nombre: ")
    print(f"\n[+] Bienvenido(a), {user_name}. Acceso concedido.") # Mensaje de bienvenida tipo hacker 
    time.sleep(0.5)
    print("="*50 + "\n")

def calculate_score(password: str) -> int:
    """Calcula un puntaje de seguridad (Máx 20 pts) basado en las reglas. """
    score = 0
    # Regla: Tiene una longitud de 8 dígitos o más. [cite: 35] (+5 pts)
    if len(password) >= 8: score += 5
    # Regla: Contienen números. [cite: 33] (+5 pts)
    if re.search(r'[0-9]', password): score += 5
    # Regla: Contiene signos especiales. [cite: 34] (+5 pts)
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password): score += 5
    # Regla: Contiene mayúsculas y minúsculas (robustez). (+5 pts)
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password): score += 5
    return score

# 1. Evaluar contraseñas (función) [cite: 26]
def evaluate_password():
    """Pide la contraseña, valida si está en débiles y evalúa su puntaje. [cite: 27]"""
    global secure_count, weak_count
    
    password = getpass.getpass("Ingrese la contraseña a probar: ")
    is_secure = False
    score = 0
    
    # Valida si está en las contraseñas débiles [cite: 27]
    if password.lower() in [p.lower() for p in WEAK_PASSWORDS]:
        print("--------------------------------------------------")
        print("❌ Contraseña encontrada en lista de contraseñas débiles.") # Mensaje de débil [cite: 29]
        print("--------------------------------------------------")
        weak_count += 1 # Incrementar variable 
    else:
        # Si no está en débiles, valida la puntuación [cite: 31]
        score = calculate_score(password)
        
        # Definición de 'segura': 15/20 o más.
        if score >= 15:
            is_secure = True
            print("--------------------------------------------------")
            print(f"✅ Contraseña segura.") # Mensaje de segura [cite: 37]
            print(f"Puntaje de seguridad: {score}/20") # Muestra puntaje [cite: 38]
            print("--------------------------------------------------")
            secure_count += 1 # Incrementar variable 
        else:
            print("--------------------------------------------------")
            print(f"⚠️ Contraseña no segura. Puntaje bajo: {score}/20")
            print("--------------------------------------------------")
            weak_count += 1 # Incrementar variable 

    # Guarda la contraseña probada en el historial [cite: 39]
    password_history.append((password, score, is_secure)) 

# 2. Mostrar contraseñas analizadas [cite: 41]
def show_history():
    """Con un ciclo, mostrar el listado de contraseñas analizadas. [cite: 42]"""
    if not password_history:
        print("\n[!] Aún no se ha analizado ninguna contraseña.")
        return

    print("\n--- Historial de Análisis ---")
    # Con un ciclo, mostrar el listado [cite: 42]
    for i, (password, score, is_secure) in enumerate(password_history):
        estado = "SEGURA (✅)" if is_secure else "DÉBIL (❌)"
        # La contraseña en sí se omite para no mostrarla en pantalla tras el análisis
        print(f"[{i+1}] Estado: {estado} | Puntaje: {score}/20")

# 3. Mostrar estadísticas [cite: 43]
def show_stats():
    """Mostrar resultado del análisis: cantidades. [cite: 44]"""
    total_analyzed = len(password_history)
    print("\n--- Estadísticas ---")
    
    # Cantidad de contraseñas que se analizaron. [cite: 45]
    print(f"Cantidad de contraseñas que se analizaron: {total_analyzed}")
    # Cantidad de contraseñas débiles [cite: 46]
    print(f"Cantidad de contraseñas débiles: {weak_count}") 
    # Cantidad de contraseñas seguras. [cite: 47]
    print(f"Cantidad de contraseñas seguras: {secure_count}") 

# --- Menú Principal (usar while)  ---
def main_menu():
    """Maneja el flujo principal con el menú interactivo."""
    welcome_message()
    
    while True: # Debe usar while 
        print("\n<<< MENÚ PRINCIPAL >>>")
        print("1. Probar una contraseña") # Opción 1 [cite: 22]
        print("2. Ver contraseñas analizadas") # Opción 2 [cite: 23]
        print("3. Mostrar estadísticas") # Opción 3 [cite: 24]
        print("4. Salir") # Opción 4 [cite: 25]
        
        try:
            opcion = int(input("Seleccione una opción (1-4): "))

            if opcion == 1:
                print("Probando Contraseña...")
                evaluate_password()
            elif opcion == 2:
                show_history()
            elif opcion == 3:
                show_stats()
            elif opcion == 4:
                print("|||Saliste del programa. ¡Adiós!|||")
                break
            else:
                print("[!] Opción no válida. Intente con 1, 2, 3 o 4.")
        except ValueError:
            print("[!] Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main_menu()