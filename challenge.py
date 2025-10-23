"""simulador de contraseñas """


print("==Laboratorio de contraseñas==")


contraseñas_analizadas = []
contraseñas_debiles = []
contraseñas_seguras = []
contraseñas_comunes = ["123", "password", "123456", "qwerty", "abc123", "login", "admin"]
caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "_"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def probador_contraseña():
    contraseña = input("Ingresa la contraseña a probar: ")
    contraseñas_analizadas.append(contraseña)
    if contraseña in contraseñas_comunes:
        print("La contraseña es muy común, intenta con otra.")
        
    elif len(contraseña) < 8:
        print("La contraseña es muy corta, intenta con otra.""\n")
        contraseñas_debiles.append(contraseña)
        
        
        
    elif not any(char in caracteres_especiales for char in contraseña):
        print("La contraseña debe incluir al menos un caracter especial.""\n")
        contraseñas_debiles.append(contraseña)
        
        
    elif not any(char in numeros for char in contraseña):
        print("La contraseña debe incluir al menos un número.""\n")
        contraseñas_debiles.append(contraseña)
        

    else:
        print("Felicidades, tu contraseña es segura.""\n")
        contraseñas_seguras.append(contraseña)
    
    return contraseña



def Mostrar_Estadistica():
    print("|||Se Analizaron|||")

    Datos = len(contraseñas_analizadas)
    print(Datos, "contraseñas""\n")
    
    Datos2 = len(contraseñas_debiles)
    print("Las", Datos2, "Son debiles")
    
    Datos3  = len(contraseñas_seguras)
    print(Datos3, "Fueron seguras""\n")   
          


if __name__ == "__main__":
    while True:
            opcion= int(input("|||Ingresa la opcion Deseada|||" "\n"
            "1. Probar una Contraseña" "\n"
            "2. Ver Contraseña Analizadas" "\n"
            "3. Mostrar Estadisticas" "\n"
            "4. Salir" "\n"
            "===============================""\n"))
            

            if opcion == 1:
                print("Probando Contraseña...")
                probador_contraseña()

            elif opcion == 2:
                    for contraseña in contraseñas_analizadas:
                        print("Contraseñas Analizadas:", contraseña, "\n")

            elif opcion == 3:
                print("Mostrando Estadisticas...")
                Mostrar_Estadistica()

            elif opcion == 4:
                print("|||Saliste del programa|||")
                break