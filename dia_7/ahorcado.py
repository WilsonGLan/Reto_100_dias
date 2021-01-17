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
# 2. Seleccionar aleatoriamente una palabra de la lista anterior.
#    Se valida el tamaño de la palabra y se agregan los '_' dentro de la variable
#    ahorcado para visualizar de cuantas letras se compone la palabra.
chosen_word = r.choice(word_list)
word_length = len(chosen_word)

for _ in range(word_length):
  ahorcado += '_'
print('La solución es:',chosen_word)
print(ahorcado)
# 3. Solicitar adivinar una de las letras y asegurarse de que sea minúscula
#    El juego debe finalizar solo cuando no hayan espacios, osea cuando se adivine
#    la palabra completa.
while '_' in ahorcado:
  guess = input('Adivina una letra\n').lower()
# 4. Revisar si la la letra se encuentra dentro de la palabra que se desea adivinar.
#    Si el usuario adivina debe asignar la letra en la posición correcta y en caso 
#    contrario colocar '_' por cada letra que no acierte.
  print("=====Resultados========")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      ahorcado[position] = letter     
  print(ahorcado)
  print("=======================")
else:
  print('You Win')
