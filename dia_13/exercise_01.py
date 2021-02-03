lista_numeros = []

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
    numero = int(input("Ingrese el primer número\t"))
    lista_numeros.append(numero)
    numero = int(input("Ingrese el segundo número\t"))
    lista_numeros.append(numero)
    continuar = input("¿Quiere ingresar más números? Escriba 'Si' o 'No' para continuar:\t")

    while continuar.upper() != 'NO':
        numero = int(input("Ingrese el siguiente número\t"))
        lista_numeros.append(numero)
        continuar = input("¿Quiere ingresar más números? Escriba 'Si' o 'No' para continuar:\t")
else:
    print("error")

