import data as d
import random as r

def choice_pokemon():
    return r.choice(d.pokemon_random)

def winner_pokemon(op):
    experience_a = poke_a["base_experience"]
    experience_b = poke_b["base_experience"]

    if experience_a > experience_b:
        if op == 'a':
            return f"El ganador es {poke_a['name']} con experiencia {experience_a} y usted obtiene 10 puntos"
        elif op == 'b':
            return f"El ganador es {poke_a['name']} con experiencia {experience_a} y usted no obtiene puntos"
    elif experience_a < experience_b:
        if op == 'a':
            return f"El ganador es {poke_b['name']} con experiencia {experience_b} y usted no obtiene puntos"
        elif op == 'b':
            return f"El ganador es {poke_b['name']} con experiencia {experience_b} y usted obtiene 10 puntos"
    else:
        return "No hay ganador, es empate"

ending = False
score = 0

while ending == False:
    poke_a = choice_pokemon()
    poke_b = choice_pokemon()

    while poke_a == poke_b:
        poke_b = choice_pokemon()


    print(f"Pokemon del equipo 'a', su nombre es: {poke_a['name']} y es de tipo {poke_a['type']}")
    print(f"Pokemon del equipo 'b', su nombre es: {poke_b['name']} y es de tipo {poke_b['type']}")

    opcion = input("Escoja 'a' o 'b' cual tiene mas base experiencia\t")
    print(winner_pokemon(opcion))

    opcion = input("Si desea continuar escriba 'Si' en caso contrario 'No':\t")
    if opcion.upper() != 'SI':
        ending = True