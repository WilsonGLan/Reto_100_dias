# ** Funciones Utilizadas**

* title()  utilizada para capitalizar o colocar la primera letra en mayúscula y las demas letras en minuscula de un string o mensaje. No necesita importar modulos.

* return Utilizado para entregar un resultado dentro de una función. No necesita importar modulos.


# ** PSEUDOCODIGO **

* ejercicio 2: Imprimir días en el mes con el metodo days_in_month(year,month). La función tiene una lista de los dias de cada mes cuando el año no es biciesto.

```
Funcion result_leap <- is_leap ( year )
	Si year % 4 = 0 Entonces
		Si year % 100 = 0 Entonces
			Si year % 400 = 0 Entonces
				result_leap = Verdadero
			SiNo
				result_leap = Falso
			FinSi
		SiNo
			result_leap = Verdadero
		FinSi
	SiNo
		result_leap = Falso
	FinSi
Fin Funcion

Funcion return <- days_in_month(eval_year, eval_month)
	tamaño <- 12	
	Dimension month_days[tamaño];
	 month_days[1] <- 31;
	 month_days[2] <- 28;
	 month_days[3] <- 31;
	 month_days[4] <- 30;
	 month_days[5] <- 31;
	 month_days[6] <- 30;
	 month_days[7] <- 31;
	 month_days[8] <- 31;
	 month_days[9] <- 30;
	 month_days[10] <- 31;
	 month_days[11] <- 30;
	 month_days[12] <- 31;	
	 
	 Si is_leap(eval_year) = Verdadero Entonces		 
		 Si eval_month = 2 Entonces			 
			 return <- 29
		 SiNo
			 return <- month_days[eval_month]
		 FinSi
	 SiNo
		 return <- month_days[eval_month]	
	 FinSi	
	
FinFuncion


Algoritmo primos
	Escribir  "Escriba el año que quiere revisar si es biciesto: "	
	Leer num_year
	Escribir  "Escriba el número del mes para el año ingresado: "
	Leer num_month
	resultado <- is_leap(num_year)
	Escribir  days_in_month(num_year, num_month)	
FinAlgoritmo
```
