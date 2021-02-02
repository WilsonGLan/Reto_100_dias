import random as r

adivinar_numero = r.randrange(1,100)

def dificultad():
    if modo_juego == 'easy':
        adivinar(10)
    elif modo_juego == 'hard':
        adivinar(5)
    else:
        "No existe esa opción"

def adivinar(x):
    numero_jugador = 0
    mensaje=""
    for intentos in range(0,x):
        print(f"You have {x-intentos} attempts remaining to guess the number.")
        numero_jugador = int(input("Make a guess:\t"))
        if intentos < x:
            if adivinar_numero == numero_jugador:
                print("You got it! The answer was 82.")
                break
            elif adivinar_numero > numero_jugador:
                print("Muy bajo")                
            elif adivinar_numero < numero_jugador:
                print("Muy alto")                
            if adivinar_numero != numero_jugador and intentos < x-1:
                print("Guess again")
            elif adivinar_numero != numero_jugador and intentos == x-1:
                print("You've run out of guesses, you lose.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
#print(f"Pssst, the correct answer is {adivinar_numero}")
modo_juego = input("Choose a difficulty. Type 'easy' or 'hard':\t")
dificultad()



