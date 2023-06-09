n = int(input())

a = []

for i in range(n):
    m = int(input())

    a.append(m) if m != 0 else a.pop()


print(sum(a))

