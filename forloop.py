def ejercicio1 ():
    for letter in "Poke center":
        print (letter)

def ejercicio2 ():
    Friends = ["Santi", "Rami", "Pablo"]
    for Friend in Friends:
        print (Friend)

def ejercicio3 ():
    for x in range(10):
        print(x)

def ejercicio4 (base_num, pow_num):
    result = 1
    for x in range (pow_num):
        result = result * base_num
    print (result)

def ejercicio5 ():

    for number in (4,3,7,8,3,4,6,8,3,45,8,2):
        if number%2==0:
            print (str(number) + " es número par")
        else:
            print (str(number) + " es número impar")


ejercicio2 ()