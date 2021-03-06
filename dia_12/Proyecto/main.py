import random as r
import art as a

adivinar_numero = r.randrange(1,100)

def dificultad():
    if modo_juego == 'easy':
        adivinar(10)
    elif modo_juego == 'hard':
        adivinar(5)
    else:
        "Option wrong"

def adivinar(x):
    numero_jugador = 0    
    for intentos in range(0,x):
        print(f"You have {x-intentos} attempts remaining to guess the number.")
        numero_jugador = int(input("Make a guess:\t"))
        if intentos < x:
            if adivinar_numero == numero_jugador:
                print(f"You got it! The answer was {adivinar_numero}.")
                break
            elif adivinar_numero > numero_jugador:
                print("Too low")                
            elif adivinar_numero < numero_jugador:
                print("Too high")                
            if adivinar_numero != numero_jugador and intentos < x-1:
                print("Guess again")
            elif adivinar_numero != numero_jugador and intentos == x-1:
                print("You've run out of guesses, you lose.")

print(a.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
#print(f"Pssst, the correct answer is {adivinar_numero}")
modo_juego = input("Choose a difficulty. Type 'easy' or 'hard':\t")
dificultad()



