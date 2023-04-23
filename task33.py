def minmax(list: list[int]) -> list[int]:
    min1 = max1 = list[0]
    for i in list:
        if i > max1:
            max1 = i
        if i < min1:
            min1 = i
    return [min1, max1]


score_list = [3, 5, 4, 4, 3, 5, 5, 3, 5]
min_max = minmax(score_list)
print(min_max)

for i in range(len(score_list)):
    if score_list[i] == min_max[0]:
        score_list[i] = min_max[1]
    elif score_list[i] == min_max[1]:
        score_list[i] = min_max[0]

print(score_list)
