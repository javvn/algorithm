
o = ["(", "["]
c = [")", "]"]

while 1:
    s = input()

    if len(s) == 1 and s == ".":
        break
    else:
        stack = []

        for i in s:
            if len(stack):
                if i in o:
                    stack.append(i)
                elif i in c:
                    if (stack[-1] == "(" and i == ")") or (stack[-1] == "[" and i == "]"):
                        stack.pop()
                    else:
                        stack.append(i)
            else:
                if i in o or i in c:
                    stack.append(i)
        print("no") if len(stack) else print("yes")
