names = ["dana", "almik", "rasul", "marisha", "nurik"]
scores = [91, 90, 95, 97, 92]

for i, name in enumerate(names):
    print(f"{i}: {name}")

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

#type checking
x = "123"
y = 456

print(type(x), type(y))
print(int(x) + y)
print(str(y) + x)

items = [10, "hello", 3.14, "aaa", [1, 3, 5], (6, 4, "sss")]

for i, item in enumerate(items):
    print(i, item, type(item))