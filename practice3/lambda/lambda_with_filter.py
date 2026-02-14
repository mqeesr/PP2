"""
filter фильтрует элементы списка
оставляя только те которые удовлетворяют условию
"""
#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#[1, 3, 5, 7]

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
less_than_5 = list(filter(lambda x: x < 5, numbers))
print(less_than_5)
#[1, 2, 3, 4]

#3
words = ["hi", "hello", "bye", "python"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)
#['hello', 'python']

#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_gt_3 = list(filter(lambda x: x % 2 != 0 and x > 3, numbers))
print(odd_gt_3)
#[5, 7]