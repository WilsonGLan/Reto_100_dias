primos_numero_uno = []
primos_numero_dos = []

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
    numero_dos = int(input("Ingrese el segundo número\t"))        
else:
    print("error")

#Descomponer los numeros ingresados en factores primos

