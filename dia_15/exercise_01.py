def buscar(array,target):
    min = 0
    max = len(array)-1
    guess = 0
    ciclo = 0
    while(max >= min):
        ciclo += 1 
        guess = int((min+max)/2)        
        if array[guess] == target:
            return guess, ciclo
        elif array[guess] < target:
            min = guess + 1
        else:
            max = guess - 1                    
    return -1, ciclo
 
primes = (2, 3, 5, 7, 11, 13,17, 19, 23, 29, 31,37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

adivinar_primo = int(input("Ingrese un número primo de 1 a 100 y te dire en que posición esta y cuantas veces fue buscado\t")) 
resultado, veces = buscar(primes,adivinar_primo)
print(f"Se encuentra en el indice {resultado} y busco {veces} veces")

