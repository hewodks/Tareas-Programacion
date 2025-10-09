class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Crear nodos
node1 = node(15)
node2 = node(3)
node3 = node(17)
node4 = node(90)
#node5 = node(32)
#node7 = node(75)

#Conectar Nodos
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
#node4.next = node5
#node5.next = node7

#Cabeza de la lista
head = node1
current = head

while current:
    print(current.data, end= "-->")
    current = current.next
print("none")

#Primero vamos al final 
current = head
while current.next:
    current = current.next

#Recorre hacia atras 
while current:
    print(current.data, end= "<---")
    current = current.prev
print("None")