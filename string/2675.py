f = input()

for i in range(int(f)):
    s = input().split(" ")

    str = ""
    l = list(s[1])

    for e in l:
        str += e * int(s[0])

    print(str)
