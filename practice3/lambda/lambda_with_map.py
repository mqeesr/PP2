"""
map просто берет те же элементы и каждый "изменяет"
"""
#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#[2, 4, 6, 8, 10]

#2
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
#[1, 4, 9, 16, 25]

#3
a = [1, 2, 3]
b = [4, 5, 6]
sum_ab = list(map(lambda x, y: x + y, a, b))
print(sum_ab)
#[5, 7, 9]

#4
numbers = [1, 2, 3, 4, 5]
indexed_mult = list(map(lambda x: x * numbers.index(x), numbers))
print(indexed_mult)
#[0, 2, 6, 12, 20]

#5
numbers = [1, 2, 3, 4, 5]
is_even = list(map(lambda x: x % 2 == 0, numbers))
print(is_even)
#[False, True, False, True, False]