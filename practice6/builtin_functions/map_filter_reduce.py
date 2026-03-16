import functools

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)

evens = list(filter(lambda x: x % 2 == 0, nums))
print("evens:", evens)

total = functools.reduce(lambda x, y: x + y, nums)
print("sum:", total)

product = functools.reduce(lambda x, y: x * y, nums)
print("product:", product)