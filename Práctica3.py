import random

def lista_de_numeros_random():
    lista_de_nums = []

    lista_de_nums.append (input("Ingrese el primer número\n"))
    lista_de_nums.append (input("Ingrese el segundo número\n"))
    lista_de_nums.append (input("Ingrese el tercer número\n"))




    print (lista_de_nums)

    print (random.choice(lista_de_nums))




def lista_practica ():

    lista_de_prueba = "1", "24", "silla", "manzana"
    lista_2 = []

    for elemento in lista_de_prueba:
        lista_2.append (elemento)
    lista_2 = sorted(lista_2, key=len)

    print (lista_2)


