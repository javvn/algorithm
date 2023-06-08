n = int(input())

c = 0

for i in range(666, 10000000):

    if '666' in str(i):
        c += 1
        if c == n:
            print(i)
            break
