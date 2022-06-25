# LIST COMPREHENSION 
# Con listas sencillas
from operator import le
from unicodedata import name


numbers = [1,2,3] # Declaro la lista con sus valores
new_numbers = [n+1 for n in numbers] # con el for recorro la lista y por cada n sumo 1 asignando el resultado a new_numbers
print(new_numbers)

# Se puede hacer lo mismo con una cadena de texto
name = 'Wilson'
letters_list = [letter for letter in name]
print(letters_list)

# Con la función range
numbers_list = [ n * 2 for n in range(1,5)]
print(numbers_list)

# Con condicional
names = ["Wilson", "Maria", "Diana", "Marcela", "Jose", "Juan", "Julio"]
short_names = [ name for name in names if len(name) <= 4]
print(short_names)
upper_names = [ name.upper() for name in names if len(name) > 4]
print(upper_names)