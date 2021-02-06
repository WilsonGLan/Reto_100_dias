def evaluar_primos(numero):            
    for evalua_primo in range(2,numero):
        if numero > 3 and numero % evalua_primo == 0:            
            return False                        
    return True

""" def lista_primos(numero_dividendo):
    primos=[]
    for numero_divisor in range(2, numero_dividendo):
        if numero_dividendo >= 2 and numero_dividendo % numero_divisor == 0 :
            if i in [2,3]:
                primos.append(i)
            elif evaluar_primos(i):
                primos.append(i)
    return primos """

def divisores_primos(numero_dividendo):
    flag = evaluar_primos(numero_dividendo) 
    if flag == True: 
        mensaje = "Es primo"
    else:
        mensaje = "No es primo"
    return mensaje

numero = int(input("Ingrese un numero:\t"))
#print(divisores_primos(numero))
print(divisores_primos(numero))