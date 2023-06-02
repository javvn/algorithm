card_len, max_num = map(int, input().split())
cards = sorted(set(map(int, input().split())))

result_arr = []

for i in range(len(cards) - 2):
    for j in range(i+1, len(cards)-1):
        for x in range(j+1, len(cards)):
            result_arr.append(cards[i] + cards[j] + cards[x])


# print(result_arr)

result_arr = sorted(list(filter(lambda l: l <= max_num, list(set(result_arr)))))


print(result_arr[-1])