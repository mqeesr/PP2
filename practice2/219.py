n = int(input())
a = list(map(int, input().split()))

maxx = -100000000
max_in = 0

for i in range(n):
    if a[i] > maxx:
        maxx = a[i]
        max_in = i

print(max_in + 1)