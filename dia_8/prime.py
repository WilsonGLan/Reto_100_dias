#Write your code below this line 👇
def prime_checker(number):
  cont_prime=0
  for n in range(1,number):
    if number%n == 0:
      if n != number and n != 1:
        cont_prime+=1
        break
  
  if cont_prime > 0:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)