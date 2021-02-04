primos_numero_uno = []
primos_numero_dos = []

#Descomponer los numeros ingresados en factores primos

def evaluar_primos(numero):            
    for evalua_primo in range(2,numero):
        if numero > 3 and numero % evalua_primo == 0:            
            return False                        
    return True

def lista_primos(numero):
    for i in range(2, numero_uno):
        if numero_uno >= 2 and numero_uno % i == 0 :
            if i in [2,3]:
                primos_numero_uno.append(i)
            elif evaluar_primos(i):
                primos_numero_uno.append(i)
    return primos_numero_uno

print("Calculadora de Minimo Común Multiplo y Mínimo Común Divisor")
print("""
=========================================
||      MENU                           ||
=========================================
|| Opción || Operación                 ||
|| 1.     || Mínimo Común Múltiplo     ||
|| 2.     || Máximo Común Divisor      ||
||        ||                           ||
=========================================
"""
)

opcion = int(input("Que opción del menú de operaciones selecciona:\t"))
if opcion in [1,2]:
    numero_uno = int(input("Ingrese el primer número\t"))    
    #numero_dos = int(input("Ingrese el segundo número\t"))     
    print(lista_primos(numero_uno))   
else:
    print("error")

