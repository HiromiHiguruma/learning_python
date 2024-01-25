mi_dicc = {"nombre": "Gaius", "edad": 29, "game": "Tales of Xillia", "año de lanzamiento": 2011, "año de lanzamiento otra vez XD": 2011}
print (mi_dicc)

#otra forma de hacer un diccionario:

mi_dicc2 = dict(nombre = "Snake", edad = 30, game = "Metal Gear Solid")

print (mi_dicc2)

print (mi_dicc2 ["nombre"])

#añadir a diccionario


mi_dicc  ["consola"] = "ps3"

print (mi_dicc)

#borrar info de dicc:

del mi_dicc ["edad"]
print (mi_dicc)

mi_dicc.pop ("consola")
print (mi_dicc)

#popitem remueve el último valor

mi_dicc.popitem()
print (mi_dicc)


#---

for valores in mi_dicc2.values():
    print (valores)

for key, value in mi_dicc2.items():
    print (key, value)



#copiar dicc:

copia_de_mi_dicc2 = mi_dicc2.copy ()

print (copia_de_mi_dicc2)

copia_de_mi_dicc2 ["mejor juego de la saga"] = 3

print (mi_dicc2)

print (copia_de_mi_dicc2)


#para fusionar datos entre diccionarios (los datos del segundo dicc se sobrescriben sobre el primer dicc)

mi_dicc.update (mi_dicc2)
print (mi_dicc)