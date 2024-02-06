#Una función lambda es una funcón de una linea sin nombre definido
#Estructura de Lambda : 
#lambda argunments : expresion

ejemplo = lambda x : x + 10

print (ejemplo(5))

ejemplo2 = lambda x, y : x * y

print (ejemplo2 (10,3))

Lista_1 = [(3,4), (100,10),(22,55)]

Lista_1_clasificada = sorted(Lista_1)

print (Lista_1_clasificada)

Lista_1_clasificada_lambda = sorted(Lista_1, key=lambda x:Lista_1[1])

print (Lista_1_clasificada_lambda)

Lista_1_ordenada_por_suma = sorted(Lista_1, key=lambda x : x[0] + x[1])

print (Lista_1_ordenada_por_suma)

Lista_2 = 1,2,3,4,5,6

Lista_2x2 = (numero*2 for numero in Lista_2 )

print (list(Lista_2x2))

#map------------------------------------------------------------
Lista_2x2_map = map(lambda x : x*2, Lista_2)

print(list(Lista_2x2_map))

#filter----------------------------------------------------------
Lista_2_filter = filter(lambda x : x%2==0, Lista_2)

print (list(Lista_2_filter))

#reduce---------------------------------------------------------

from functools import reduce

Lista_2_reduce = reduce(lambda x,y : x*y, Lista_2)

print (Lista_2_reduce)