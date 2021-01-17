from replit import clear
import random as r
import arte_ahorcado as art
import palabras_ahorcado as p

print(art.logo,'\n')

lost_lives = 0
ahorcado=[]

chosen_word = r.choice(p.word_list)
word_length = len(chosen_word)

for _ in range(word_length):
  ahorcado += '_'

print(f"{' '.join(ahorcado)}\n")

while lost_lives < 6 and '_' in ahorcado:  
  guess = input('Adivina una letra\n').lower()

  clear()

  if guess in chosen_word:
    print("=====Resultados========")
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        ahorcado[position] = letter
        print(f"Usted adivino la letra {guess}\n")        
  else:
    lost_lives +=1    
    print(f"Parece que la letra {guess} no es la correcta\n")
  print(art.lives[lost_lives],'\n')
  print(f"{' '.join(ahorcado)}\n")
  print("=======================\n")

if '_' not in ahorcado:
  print('Tu ganas')
else:
  print(f'Tu pierdes, la respuesta correcta es: {chosen_word}')
