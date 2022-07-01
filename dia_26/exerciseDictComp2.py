
import pandas

student_dict = {
    "Student": ["Wilson", "Maria", "Diana", "Marcela", "Jose", "Juan", "Julio"],
    "Score": [56, 76, 98, 40, 75, 32, 85]
}

print(student_dict)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.Student, " ", row.Score)