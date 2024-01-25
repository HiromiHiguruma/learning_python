#los sets no admiten duplicados, se pueden modificar, no tienen órden específico


mi_set = {1,2,3}
print (mi_set)

mi_set2= set([4,5,6])
print (mi_set2)

#añadir y eliminar elementos al set


mi_set3 = set()

mi_set3.add ("ping pong")
mi_set3.add (3)
mi_set3.add ("cuack")

print (mi_set3)
#para remover tamien se puede usar.discard() y no va a tirar error si no encuentra el elemento 
mi_set3.remove ("ping pong")
print (mi_set3)

def cuom ():
    score = 0
    for x in mi_set3:
        print (str(score) + " "+ str(x))
        score = score + 1



set_numeros_pares = {0,2,4,6,8,10}
set_numeros_impaeres = {1,3,5,7,9}
set_numeros_primos = {2,3,5,7}
# .union() es para combinar 2 sets
set_pares_e_impares = set_numeros_pares.union(set_numeros_impaeres)
print (set_pares_e_impares)
# .intersection() solo conseva los valores que se repiten en las 2 listas

set_interseccion_pares_y_primos = set_numeros_pares.intersection(set_numeros_primos)
print (set_interseccion_pares_y_primos)


set_interseccion_impares_y_primos = set_numeros_impaeres.intersection(set_numeros_primos)
print (set_interseccion_impares_y_primos)


# .difference() solo conserva los valores que no se de la primera lista, .symemtricdifference() solo conserva los valores que no se repiten en las 2 listas

set_frutas = {"banana", "manzana", "uva", "sandia"}

set_comida_pref = {"uva", "hamburguesa", "milanesa"}

set_comida_mala = set_frutas.difference(set_comida_pref)

print (set_comida_mala)


# .issubset () sirve para corroborar si una parte de un set está dentro de otra ej: setA = {1,2,3} setB = {1,2,3,4,5,6,7,8,9}
#setA es subset de setB
# .issuperset () es lo contrario a .subset ()

# .isdisjoint es para corroborar si no hay elementos que se repiten en 2 sets

#frozen set no se puede modificar
set_congelado = frozenset ([1,2,3,4,5,6,7,8,9])
