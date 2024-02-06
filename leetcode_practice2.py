def twosum (lista_de_numeros, target):

    diccionario = dict()

    for nro_index, numero in enumerate(lista_de_numeros):

        diccionario [numero] = nro_index

    for rango in range (0, len (lista_de_numeros)):

        resultado = target - lista_de_numeros [rango]

        if resultado in diccionario and rango != diccionario [resultado]:

            return [rango, diccionario [resultado]]



lista = [3,2,4]

numero_target = 6

print (twosum (lista, numero_target))






def firstUniqChar(s):

    for letter in s:

        if s.count (letter) == 1:

            return s.index (letter)
        
    return -1

            


mi_string = "chumc"

print( firstUniqChar (mi_string))
