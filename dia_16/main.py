from turtle import Turtle, Screen
import sys
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")

timmy.home() #Pone a timmy en el origen
timmy.circle(50) #Dibuja un circulo completo donde tiene un radio de 50 pixeles
timmy.circle(120, 90) #Dibuja un semicirculo con 120 pixeles de radio y un angulo de 90 grados
print(timmy.forward(100)) #Moviendo la tortuga 100 pixeles adelante
timmy.circle(120, 180)
print(timmy.forward(100))
timmy.circle(120, 90)
my_screen = Screen()
#print(my_screen.canvheight)
my_screen.exitonclick() #La ventana se cierra hasta que se haga un click 


