def evaluar_primos(numero):            
    for evalua_primo in range(2,numero):
        if numero > 3 and numero % evalua_primo == 0:            
            return False                        
    return True

def lista_primos(numero_dividendo):
    primos=[]
    for numero_divisor in range(2, numero_dividendo+1):
        if numero_dividendo >= 2 and numero_dividendo % numero_divisor == 0 :
            if numero_divisor in [2,3]:
                primos.append(numero_divisor)
            elif evaluar_primos(numero_divisor):
                primos.append(numero_divisor)
    return primos

def divisores_primos(numero_dividendo):
    numero_cociente = numero_dividendo
    lista_primos = []
    for numero_divisor in range(2,numero_dividendo+1):
        if numero_dividendo % numero_divisor == 0:
            es_primo = evaluar_primos(numero_divisor)         
            while es_primo:                        
                lista_primos.append(numero_divisor)
                numero_cociente = numero_cociente / numero_divisor
                if numero_cociente % numero_divisor != 0:
                    es_primo = False
            if numero_cociente == 0:
                break
    return lista_primos

def factores_primos(numero_dividendo):
    factores_unicos = lista_primos(numero_dividendo)
    total_factores = divisores_primos(numero_dividendo)
    cantidad_factores = {}    
    for factor in factores_unicos:
        cantidad_factores[factor] = total_factores.count(factor)
    return cantidad_factores        


numero = int(input("Ingrese un numero:\t"))
#print(divisores_primos(numero))
print(divisores_primos(numero))
print(lista_primos(numero))
print(factores_primos(numero))