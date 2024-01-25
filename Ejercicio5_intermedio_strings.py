#se pueden usar tanto "" como '' para emepzar y terminar un string
print ("Hola")
print ('Chau')

print ("""SE PUEDE USAR
TRIPLE COMILLAS
PARA ESCRIBIR EN
VARIAS LÍNEAS """)

#Acceder a index, ejemplos:
Dragon_ball = "Dragon Ball"
print (Dragon_ball[0:6])

#Los strings son inmutables/no se pueden cambiar.

Dragon_ball_reverse = Dragon_ball [::-1]
print (Dragon_ball_reverse)

print (Dragon_ball.upper())

print (Dragon_ball.lower())

print (Dragon_ball.startswith("Dragon"))

# de string a lista:
# .split () utiliza espacios para dividir los elementos, si se quiere que el criterio sea otro se pone entre los parentesis
mi_string = "Buenos días Mandy"
mi_lista = mi_string.split()

print (mi_lista)

#de lista a string:

mi_lista2 = ["You", "are", "my", "special"]
#lo que se pone entre comillás es lo que va a separa a los elementos una vez que se forme el string, si no se pone nada
#los elementos van a salir pegados en el string

mi_string2 = " ".join(mi_lista2)

print (mi_string2)

#formas de añadir una variabla a un string

mi_variable = "bobo"

#si la variable es un número entero se usa %d y si es un decimal se usa %f (por default mostrara los últimos 6 dígitos del decimal, pero se puede especificar la cantidad deseada
#poniendo .número despues del %. EJ: %.2f )
mi_string3 = "¿Qué mirás %s?" % mi_variable

print (mi_string3)
#-----------------------------------------------------------------
mi_variable2= "cancha"

mi_string4 = "Andá a la {} {}".format(mi_variable2, mi_variable)

print (mi_string4)
#---------------------------------------------------------------

mi_string5 = f"Ya estoy en la {mi_variable2}, {mi_variable}"
print (mi_string5)