import math

f = input()

arr = []

for i in range(int(f)):
    arr.append(int(input()))

change = [25, 10, 5, 1]


for e in arr:
    r = []
    temp = e
    for c in change:
        # print(temp, c, math.floor(temp / c))
        r.append(str(math.floor(temp / c)))
        temp = temp - c * math.floor(temp / c)
    print(' '.join(r))