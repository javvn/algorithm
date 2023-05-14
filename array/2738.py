# def add_one(n):
#     return n + 1

f = list(map(int, input().split()))

a = []
b = []
result = []

for i in range(f[0] * 2):
    if i < f[0]:
        a.append(list(map(int, input().split())))
    else:
        b.append(list(map(int, input().split())))


for idx, i in enumerate(a):
    temp = []
    for idxx, j in enumerate(i):
        temp.append(j + b[idx][idxx])

    result.append(temp)

for r in result:
    print(' '.join(str(e) for e in r))