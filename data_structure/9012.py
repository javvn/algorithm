f = int(input())

for i in range(f):
    x = list(input())
    temp = []
    for e in x:
        if e == "(":
            temp.append(e)
        else:
            if not len(temp) == 0:
                if temp[len(temp) - 1] == "(":
                    temp.pop()
            else:
                temp.append(e)

    print("NO" if len(temp) else "YES")
