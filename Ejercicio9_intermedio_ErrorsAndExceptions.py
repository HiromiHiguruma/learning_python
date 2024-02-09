#para definir un error se puede hacer con el  siguiente método

mi_variable = 4

if mi_variable > 5:

    raise Exception ("mi_variable no puede ser mayor que 5")

#también se puede hacer de esta manera 

mi_variable2 = 49

assert (mi_variable2 != 50) , "mi_variable2 debe equivaler a 50"

#try y except

try : 
    mi_variable3 = 5/0
except ZeroDivisionError:

    print ("Che flaco sos pelotudo vos? No se puede dividir por cero. Te falla no?")


#podés "agarrar" los errores y personalizar el mensaje que querés que salga. si hacés esto el código va a seguir ejecutandose después del except

try:

    print (mi_variable4)

except NameError as exepcion:

    print (exepcion)

#para definir errores "propios" se puede hacer de esta manera también:
    
class EL_NUMERO_ES_MUY_ALTO_ERROR (Exception):
    pass

def Si_es_mas_que_100_tira_error (valor):
    if valor > 100:
        raise EL_NUMERO_ES_MUY_ALTO_ERROR ("Te fuiste al choto man, poné un número mas chico")


Si_es_mas_que_100_tira_error (500)