s = input().split()

print(int(''.join(reversed(s[0])))) if ''.join(reversed(s[0])) > ''.join(reversed(s[1])) else print(int(''.join(reversed(s[1]))))