from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

def caesar (choice_direction, text_send, number_shift):
  cipher_text=''
  for i in range(0,len(text_send)):
    if text_send[i] in alphabet:
      if choice_direction == 'encode':
        cipher_text += alphabet[alphabet.index(text_send[i])+number_shift]
      else:
        cipher_text += alphabet[alphabet.index(text_send[i])-number_shift]
    else:
      cipher_text += text_send[i]
  print(f'The {choice_direction}d text is: {cipher_text}')

print(logo)

should_end = False

while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  caesar(direction, text, shift)  

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Bye")