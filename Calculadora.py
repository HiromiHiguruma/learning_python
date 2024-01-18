valor1 = input ("Ingrese el primer número ")
valor2 = input ("Ingrese el segundo número ")


print ("La suma entre " + valor1 + " y " + valor2 + " es de " + str (float(valor1) + float(valor2))+".") 
print ( )
print ("La resta entre " + valor1 + " y " + valor2 + " es de " + str (float(valor1) - float(valor2))+".") 
print ( )
if valor1 != valor2:
    print ("La resta entre " + valor2 + " y " + valor1 + " es de " + str (float(valor2) - float(valor1))+".") 
print ( )
print ("La multiplicación entre " + valor1 + " y " + valor2 + " es de " + str (float(valor1) * float(valor2))+".") 
print ( )
print ("La división entre " + valor1 + " y " + valor2 + " es de " + str (float(valor1) / float(valor2)) + " y su resto es de " + str(float(valor1) % float(valor2)) +".")
print ( )
if valor1 != valor2:
    print ("La división entre " + valor2 + " y " + valor1 + " es de " + str (float(valor2) / float(valor1)) + " y su resto es de " + str(float(valor1) % float(valor2)) +".")


input ("Presiona Enter para terminar.")