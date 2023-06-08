# s = input()
#
# l, n = len(s), int(s)
#
# x, r = [i for i in range(1, 10)], []
#
#
# def dup_comb(array, _r):
#     for i in range(len(array)):
#         if _r == 1:
#             yield [array[i]]
#         else:
#             for _next in dup_comb(array[0:], _r-1):
#                 yield [array[i]] + _next
#
#
# dup_filter = list(filter(lambda z: z[0] <= int(s[0]), dup_comb(x, l)))
#
# for i in dup_filter:
#     d, dd = 0, 0
#     for k, v in enumerate(range(l-1, -1, -1)):
#         dd += i[k]
#         d += i[k] * (10 ** v)
#
#     if n == d + dd:
#         r.append(d)
#
#
# print(dup_filter)
# print(list(reversed(sorted(r)))[-1] if r else 0)

m = int(input())

for i in range(1, m+1):
    n = i + sum(list(map(int, str(i))))

    if m == n:
        print(i)
        break

    if i == m:
        print(0)

