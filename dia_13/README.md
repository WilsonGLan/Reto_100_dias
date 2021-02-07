# **Día 13**
---
### Mínimo Común Múltiplo y Máximo Común Divisor

Ejercicio 1: 
 * Crear un programa que permita elegir al usuario si desea calcular el m.c.m. o el m.c.d. 
 * El usuario solo puede ingresar dos números para calcular la opción elegida.
 * El programa debe mostrar el resultado final.

 Nota: Durante el desarrollo del ejercicio se observó que existen varias maneras de calcular tanto el m.c.m como el m.c.d. y se trató de realizar el código con menos lineas, sin embargo podría reducirse más ya que python tiene una función dentro del módulo `math` llamado `gcd()` el cual calcula el m.c.d. sin embargo solo ahorraria 2 lineas teniendo en cuenta que puedo calcular primero el m.c.m. y con ello luego el m.c.d.. También existe una función llamada `lcm()` que tambien recibe dos números pero solo esta disponible a partir de la versión 3.9 de python y actualmente este programa funciona con la versión 3.8


### Números primos
 Ejercicio 2:
 * Programa que permita conocer los factores primos que pertenecen a un número entregado por el usuario y cuantas veces se repite cada uno.
 * Para realizar este ejercicio se toma en cuenta que los números primos son aquellos que solo son divisibles entre 1 y el mismo número, por lo que si llega a ser divisible por otro numero menor a él mismo entonces no es primo.
 * Se mostrará en pantalla cada factor con su correspondiente exponente