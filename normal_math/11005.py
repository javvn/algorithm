import math

f = input().split()
arr = list(map(int, f))

r = ""

while arr[0] != 0:
    r += str(arr[0] % arr[1]) if arr[0] % arr[1] < 10 else chr(arr[0] % arr[1] + 55)
    arr[0] = math.floor(arr[0] / arr[1])

print(''.join(list(reversed(r))))