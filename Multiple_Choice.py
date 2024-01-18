from Multiple_choice_object import Pregunta



array_de_preguntas = [
    ["¿De que color es la frutilla?  \nOpción: A) Roja \nOpción: B) Azul\nOpción: C) Amarilla \n", "a"],
    ["\n¿En que año se firmó la declaración de independencia de Argentina?\nOpción A) 1660\nOpción B) 1916\nOpción C) 1987\n","b"],
    ["\n¿Cuál de estas opciones es la capital de España?\nOpción A) Madrid\nOpción B) Valencia\nOpción C) Barcelona\n","a"]
]


preguntas = [
Pregunta(array_de_preguntas[0][0],array_de_preguntas[0][1]),

Pregunta (array_de_preguntas[1][0],array_de_preguntas[1][1]),

Pregunta(array_de_preguntas[2][0],array_de_preguntas[2][1])

]

def quiz (x):
    score = 0
    for pregunta in x:
        respuesta_del_usuario = input (pregunta.premisa)
        if  respuesta_del_usuario.lower() == pregunta.respuesta_correcta:
            score+=1
        
    print ("Respuestas correctas: " + str(score) + "/" + str(len(x)) )





quiz (preguntas)
input ("enter to exit")