mi_lista = ["Goku", "Vegeta", 8000, True]

for x in mi_lista:
    print (x)

mi_lista.append ("Raditz")
print (mi_lista)

mi_lista.insert (2, "Gohan")
print (mi_lista)


#pop--> saca un elemento de la lista por número de index, si se deja sin ningún numero de index saca el último elemento de la lista.
goku = mi_lista.pop (0)
print (mi_lista)

mi_lista.remove (True)
print (mi_lista)

mi_lista.reverse()
print (mi_lista)

mi_lista.clear ()
mi_lista.append ("Nappa")
print (mi_lista)
print (mi_lista * 10)



mi_lista2 = ["sushi", "Ramen", "Takoyaki", "Empanada", "Pizza"]
print (mi_lista2)
print (mi_lista2 [0:4])
# :: es para hacer intervalos
print (mi_lista2[::2])



#Si no se usa el .copy () los las 2 listas mi_lista2 y copia_de_mi_lista2 van a tener exáctamente el mismo valor, ergo acciones tomadas sobre
#copia de copia_de_mi_lista2 van a afectar directamente a mi_lista2 
#También se puede usar mi_lista copia_de_mi_lista2 = mi_lista2 [:] para obtener el mismo resultado que con .copy ()


copia_de_mi_lista2 = mi_lista2.copy ()

copia_de_mi_lista2.append ("Chorizo")

print (mi_lista2)
print (copia_de_mi_lista2)