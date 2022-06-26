# 1 Create a new list called squared_numbers with the list of numbers squared
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

# 2 print numbers even
result = [n for n in numbers if n % 2 == 0]
print(result)

# Whith Files

with open("D:/GITHUB_REPOSITORIOS/Reto_100_dias/dia_26/file1.txt") as file1:
    list1 = file1.readlines()
print(list1)
with open("D:/GITHUB_REPOSITORIOS/Reto_100_dias/dia_26/file2.txt") as file2:
    list2 = file2.readlines()
print(list2)
result = [int(num) for num in list1 if num in list2]

print(result)
