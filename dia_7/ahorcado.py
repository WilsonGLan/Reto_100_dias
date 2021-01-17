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

# 1. Crear una lista de palabras para adivinar
word_list=['trabajando', 'biblioteca', 'fabrica']
# 2. Seleccionar aleatoriamente una palabra de la lista anterior
chosen_word = r.choice(word_list)
# 3. Solicitar adivinar una de las letras y asegurarse de que sea minúscula
guess = input('Adivina una letra\n').lower()
# 4. Revisar si la la letra se encuentra dentro de la palabra que se desea adivinar.
print("=====Resultados========")
for letter in chosen_word:
  if letter == guess:
    print('Right')
  else:
    print('Wrong')
print("=======================")