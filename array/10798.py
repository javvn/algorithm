arr = []

max_len = 0
result = ""

for i in range(5):
    arr.append(input())
    if max_len < len(arr[i]):
        max_len = len(arr[i])

for i in range(max_len):
    for j in arr:
        try:
            result += j[i]
        except IndexError:
            pass


print(result)