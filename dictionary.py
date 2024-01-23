conversor_de_nombres = {
    "Martin":"Tincho",
    "Nicolás":"Nico",
    "Santiago":"Santi",
    "Alejandro":"Ale"
    }

print (conversor_de_nombres.get("Pedro", "No hay nadie con ese nombre"))

height = 12
for i in range(0,height):
    print("/" * (height - i))