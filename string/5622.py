s = list(input())
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

times = 0

for i in s:
    for idx, v in enumerate(dial):
        if i in list(v):
            times += idx + 3
            break


print(times)