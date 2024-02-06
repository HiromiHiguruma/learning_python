#itertools son herramientas para manejar contenedores (listas, tuplas,etc.)

#product
from itertools import product

#El producto sirve para combinar en contenedores separados los elementos de un contenedor combinados con otro contenedor

Lista_1 = [1,2]

Lista_2 = [3,4]

Producto = product(Lista_1, Lista_2)

print (list(Producto))

Lista_3 = [1,2]

Lista_4 = [3]

#--------------------------------------------------

Producto2 = product(Lista_3, Lista_4, repeat = 2)

print (list(Producto2))


#--------------------------------------------------

from itertools import permutations

#permutation devuelve todas las combinaciones posbiles

Lista_5 = [8,9,10]

permutacion = permutations (Lista_5)

print (list(permutacion))

#se puede aclarar la cantidad de elementos en la lista 

permutacion2 = permutations (Lista_5, 2)

print (list(permutacion2))
#---------------------------------------------------------

from itertools import combinations

#Las combinaciones muestran combinaciones con una cantidad especificada (es obligatorio especificar) de elementos. No se combinan los mismos elementos.


Lista_6 = [11,12,13,14]

combinacion = combinations (Lista_6, 2)

print (list(combinacion))

#las combinaciones con remplazo son lo mismo solo que los elementos si se combinan con ellos mismos.
from itertools import combinations_with_replacement

Lista_7 = [15,16,17,18]

combinacion_con_reemplazo = combinations_with_replacement(Lista_7,2)

print (list(combinacion_con_reemplazo))
#------------------------------------------------------------
from itertools import accumulate
#acumulate sirve para realizar operaciones sobre los elementos de las lista.Se empieza del índice 0 y 1, y va prosiguiendo aplicando el resultado de la operación 
#con el número siguiente
#Por defecto realiza suma

Lista_8 = [10,20,30]

acumulacion = accumulate (Lista_8)
print (list(acumulacion))

#si se quiere realizar otra operación que no sea suma
import operator

acumulacion_multiplicada = accumulate (Lista_8 , func=operator.mul)

print (list(acumulacion_multiplicada))

#---------------------------------------------------------
#groupby organiza los elementos dentro de un contenedor mediante un criterio generalmente expresado con una función
from itertools import groupby
Lista_10 = [1,2,3,4,5,6,7,8,9]

def mayor_a_5 (x):
    return x > 5

grupo_por = groupby (Lista_10, key= mayor_a_5)
for key, value in grupo_por:
    print (key, list(value))
#-------------------------------------------------------------------
#iterdores infinitos: count (contar), cycle (ciclo), repeat (repetir)
from itertools import count

#count empieza a contar desde un valor dado de forma infinita
#se puede utilizar un if y break para determinar donde se termina de ejecutar el código
for numero in count (10):
    print (numero)
    if numero == 1000:
        break
#cycle repite los elementos de un contenedor hasta que ponga una condición para detenerlo
from itertools import cycle
    
Lista_11 = ["Pim", "Pum", "Pam"]

for palabra in cycle(Lista_11):
    print (palabra)
    if palabra == "Pam":
        break

#repeat repite elementos de contenedores hasta una determinada cantidad de veces
from itertools import repeat

for palabra in repeat(Lista_11 [0:], 5):
    print (palabra)

