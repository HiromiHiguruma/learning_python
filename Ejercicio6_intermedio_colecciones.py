#tipos de colleciones : counter, namedtuple, ordered dict, default dict, deque
#counter:
from collections import Counter
#guarda los contenidos como keys de diccionario, y su cantidad como valor de diccionario

mi_string = "aaaaabbbc"
mi_counter = Counter(mi_string)
print (mi_counter)

print (mi_counter.keys())

print (mi_counter.values())

print (mi_counter.items())

#para ver el elemento que más se repite
print (mi_counter.most_common(1))

#tambien se puede acceder a la tupla que da .most_common () poniendo coordenadas:

print (mi_counter.most_common(1)[0] [0])


#esto "separa" el string con un for loop y pone todos sus caracteres como elementos particulares
print (mi_counter.elements ())
#para que se vea hay que pasarlo a lista
print (list (mi_counter.elements ()))



from collections import namedtuple
#para crear objetos de forma rápida (solo con 2 elementos)

ecuacion_estructura = namedtuple ("ecuacion", "x,y")
ecuacion1 = ecuacion_estructura(3,5)

print (ecuacion1)
print (ecuacion1.x, ecuacion1.y)


from collections import OrderedDict

#son como diccionarios normales pero recuerdan el órden en que se agregan objetos:
#obsoleto en python 3.7

diccionario_ordenado = OrderedDict ()
diccionario_ordenado ["a"] = 1
diccionario_ordenado ["b"] = 2
diccionario_ordenado ["c"] = 3
diccionario_ordenado ["d"] = 4

print (diccionario_ordenado)


from collections import defaultdict

#el defaultdict da un valor predeterminado (int,str,float) a los keys que no tienen asignado uno
diccionario_default = defaultdict(int)
diccionario_default ["a"]= 1
diccionario_default ["b"]= 2
diccionario_default ["c"]= 3
print (diccionario_default["d"])

from collections import deque

#es un contenedor al cual se le puede agregar o quitar elementos por izquierda y por derecha

mi_deque = deque()

mi_deque.append(1)
mi_deque.append(2)
mi_deque.append(3)
mi_deque.appendleft("gato")
mi_deque.appendleft (67)

print (mi_deque)
mi_deque.rotate(1)
print (mi_deque)

