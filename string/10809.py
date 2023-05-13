str = input()

# str = list("asd")
alpha = list("abcdefghijklmnopqrstuvwxyz")

for i in alpha:
    print(str.index(i)) if i in str else print(-1)


