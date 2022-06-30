'''
# Permite crear un nuevo diccionario a partir de los valores de una lista o un diccionario

new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dict.items()}

'''
import random as r

# Entonces creamos un diccionario por medio de una lista
names = ["Wilson", "Maria", "Diana", "Marcela", "Jose", "Juan", "Julio"]
student_scores = {student:r.randint(1, 100) for student in names}
print(student_scores)

# Recorremos el diccionario anterior para mostrar solo los que aprueben la condición
passed_students = {student:score for student, score in student_scores.items() if score >= 60}
print(passed_students)