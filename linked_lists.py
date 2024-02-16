#las linked lists son listas que estan compuestas por estructuras de datos llamadas nodos
# el primer nodo es usualmente llamado "head node" 
#todos los nodos tienen 2 elementos separados los cuales son el valor y puntero (pointer)
#el puntero apunta al SIGUIENTE NODO en una linked list
#al final de una linked list siempre está el último nodo el cual es comunmente llamado "tail node"
#el tail node siempre apunta a null/none, lo que indica que no hay mas nodos en esa linked list
# hay varios tipos de linked lists
#los mas comunes son singly y doubly linked list
# en una singly linked list cada nodo apunta SOLAMENTE al siguiente nodo y nada más
# en una doubly linked list los nodos apuntan tanto al siguiente nodo como al anterior nodo
#---------------------------------------------------------------------------------------------

class linked_list_node:

    def __init__(self, value, next_node = None):
        
        self.value = value

        self.next_node = next_node


#acá tenemos los nodos por separado, los cuales apuntan naturalmente a None ya que no están conectados

node1 = linked_list_node (3)

node2 = linked_list_node (76)

node3 = linked_list_node (100)

#se conectan de esta forma:

node1.next_node = node2 #Lo que esto quiere decir es que el nodo1 está apuntando al nodo2
node2.next_node = node3

#forma para ver la linked list:

nodo_de_pruba = node1

lista = []

while nodo_de_pruba != None:


    lista.append (nodo_de_pruba.value)

    nodo_de_pruba = nodo_de_pruba.next_node

print (lista)


#--------------------------------------------------------------------------------------------------

nodo_de_pruba = node1

while nodo_de_pruba:

    print (nodo_de_pruba.value)

    nodo_de_pruba = nodo_de_pruba.next_node

#--------------------------------------------------------------------------------------------------
