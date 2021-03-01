""" 
import colorgram


rgb_colors =[]
colors = colorgram.extract("dia_18/image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors) """

import turtle as turtle_module
import random


turtle_module.colormode(255) #Especifico colores tipo RGB
tim = turtle_module.Turtle() #Creo un objeto llamado tim de tipo Turtle
tim.penup()                  #Indico que oculte la linea de desplazamiento
tim.hideturtle()             #Indico que oculte la tortuga

color_list = [(241, 227, 205), (196, 162, 115), (213, 228, 240), (242, 220, 231), (218, 240, 229), (130, 166, 189), (66, 101, 133), (186, 145, 164), (136, 71, 96), (134, 177, 156), (143, 91, 63), (219, 204, 129), (169, 160, 53), (66, 118, 89), (125, 33, 55), (178, 95, 119), (67, 27, 48), (86, 154, 126), (194, 98, 77), (221, 173, 190), (66, 36, 22), (31, 42, 69), (162, 209, 191), (72, 153, 169), (108, 120, 165), (230, 174, 163), (45, 54, 104), (180, 185, 215), (154, 207, 217), (120, 39, 30)] 

tim.setheading(135) # Apunto la tortuga a 135 grados
tim.forward(300)    # Muevo la tortuga 300 pasos
tim.setheading(0)   # Reinicio la orientación de la tortuga
number_of_dots = 500# Indica cuantos puntos voy a dibujar

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # Selecciono un color aleatoriamente y lo pinto
    tim.forward(20)                         # Avanzo 20 pasos

    if dot_count % 25 == 0:
        tim.setheading(270) # Apunto la tortuga 270 grados
        tim.forward(20)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

