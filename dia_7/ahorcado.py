import random as r
print('''    
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
      |
==========
'''
)
ahorcado=[]
# 1. Crear una lista de palabras para adivinar
word_list=['trabajando', 'biblioteca', 'fabrica']
# 2. Seleccionar aleatoriamente una palabra de la lista anterior
chosen_word = r.choice(word_list)
print('La solución es:',chosen_word)
# 3. Solicitar adivinar una de las letras y asegurarse de que sea minúscula
guess = input('Adivina una letra\n').lower()
# 4. Revisar si la la letra se encuentra dentro de la palabra que se desea adivinar.
#    Si el usuario adivina debe asignar la letra en la posición correcta y en caso 
#    contrario colocar '_' por cada letra que no acierte.
print("=====Resultados========")
for letter in chosen_word:
  if letter == guess:
    ahorcado.append(letter)
  else:
    ahorcado.append('_')
print(ahorcado)
print("=======================")