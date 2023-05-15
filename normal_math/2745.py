arr = input().split()

r = 0

for index, c in enumerate(list(reversed(arr[0]))):
    if ord(c) >= 65:
        r += int(arr[1])**index * (ord(c)-55)
    else:
        r += int(arr[1])**index * int(c)

print(r)
