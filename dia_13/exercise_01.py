primos_numero_uno = []
primos_numero_dos = []

#Descomponer los numeros ingresados en factores primos

def evaluar_primos(numero):
    if numero > 1:
        contar_divisores = 0
        for evalua_primo in range(2,numero):
            if numero > 3 and numero % evalua_primo == 0:
                contar_divisores += 1
                return contar_divisores                
            elif numero - 1 == evalua_primo:
                return contar_divisores


def lista_primos(numero):
    for i in range(2, numero_uno):
        if numero_uno >= 2 and numero_uno % i == 0 :
            if i in [2,3]:
                primos_numero_uno.append(i)
            elif evaluar_primos(i) == 0:
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
else:
    print("error")

print(lista_primos(numero_uno))