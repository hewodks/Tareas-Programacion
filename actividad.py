from graphviz import Digraph

dot = Digraph()

#primera capa
dot.node('A', 'Raíz')
dot.node('B', 'Izquierda')
dot.node('C', 'Derecha')

#segunda capa
dot.node("D", "Derecha")
dot.node("E", "Perro", color = "Blue",)
dot.node("F", "Derecha")
dot.node("G", "Izquierda")

dot.edges(["AB", "AC"])
dot.edges(["CD", "BE"])
dot.edges(["BF", "CG"])

dot.render("Arbol_Simple2", view=False)
