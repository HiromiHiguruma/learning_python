#los parentesis son opcionales en tupla
mi_tupla = ("Fushiguro", "Yuji", True, 69)
print (mi_tupla)
#Podés transformar una lista en una tupla usando el iterable tuple()
mi_lista = ["Nobara", "Nanami", False, 84]
mi_tupla2 = tuple(mi_lista)
print (mi_tupla2)



print (mi_tupla.count(69))

print (mi_tupla.index("Fushiguro"))

pelo_negro, sukuna, booliano, numero = mi_tupla

print (pelo_negro)
