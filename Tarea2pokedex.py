
Global = []

def Ingresa_Pokemon():
    Nombre = input("Ingresa su nombre: ")
    Tipo = input("Tipo de mo: ")
    PS_Vida = int(input("Cuanta vida tiene: "))

    Pokemon = {
        "nombre" : Nombre,
        "tipo" : Tipo,
        "PS" : PS_Vida
    }
    Global.append(Pokemon)

    print("Quieres agregar uno mas?")
    Agregarmas = input("SI | NO" "\n" ":")
    if Agregarmas == "SI":
        Ingresa_Pokemon()
    else: 
        print("Vuelve a Seleccionar la Opcion: ")

def Ver_Lista():
    for i in Global:
        print(i)

def Eliminar_Pokimon():
    Elimi = int(input("Ingresa el numero de Pokemon que deseas eliminar: "))
    Global.pop(Elimi)
    print("El numero 1 a sido eliminado")


while True:
    print("Bienvenido a Pokemon")
    print()
    print("||| Pokedex |||" "\n"
    " ||| Menu  |||")
    print("1. Ingresar" "\n" "2. Ver Pokemones" "\n" "3. Eliminar Pokemons" "\n" "4. Salir")
    Ingresar = int(input(":")) 
    
    if Ingresar == 4:
        print("fin")
        break

    elif Ingresar == 1:
        Ingresa_Pokemon()

    elif Ingresar == 2:
        Ver_Lista()

    elif Ingresar == 3:
        Eliminar_Pokimon()

