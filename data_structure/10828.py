import sys

f = int(input())
data = [sys.stdin.readline().strip() for i in range(f)]
stack = []

for d in data:
    cmd = d.split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "top":
        print(stack[len(stack) - 1] if len(stack) else -1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1 if not len(stack) else 0)
    elif cmd[0] == "pop":
        print(stack.pop() if len(stack) else -1)

