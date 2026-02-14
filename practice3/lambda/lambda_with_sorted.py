#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#[('Tobias', 22), ('Emil', 25), ('Linus', 28)]
"""
sorted(..., key=...) — sorts by key which returns lambda
lambda x: x[1] takes ages
"""

#2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
#['pie', 'apple', 'banana', 'cherry']

#3
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_desc)
#[('Linus', 28), ('Emil', 25), ('Tobias', 22)]

#4
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28), ("Al", 30)]
sorted_by_name_len = sorted(students, key=lambda x: len(x[0]))
print(sorted_by_name_len)
#[('Al', 30), ('Emil', 25), ('Linus', 28), ('Tobias', 22)]