
Alumnos = []
    

def Incerta_Alumnos():
    Diccionario = {
        "Nombre": "", 
        "Edad": 0,
        "Carrera": ""
    }
    Nombre = input("Ingresa tu nombre: ")
    Edad = int(input("Ingresa tu edad: "))
    Carrera = input("Ingresa tu carrera: ")

    Diccionario["Nombre"] = Nombre
    Diccionario["Edad"] = Edad
    Diccionario["Carrera"] = Carrera
    Alumnos.append(Diccionario)
    print(Alumnos)

    
Incerta_Alumnos()
Incerta_Alumnos()
Incerta_Alumnos()