from math import inf

length = int(input())

nums = [[inf] * length for _ in range(length)]
for i in range(length):
    nums[i][i] = 0

for i in range(length):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    nums[a][b] = c
    nums[b][a] = c

for i in range(length):
    for j in range(length):
        for k in range(length):
            expr = nums[i][k] + nums[k][j]

            if nums[i][j] > expr:
                nums[i][j] = expr
for x in range(1, length + 1):
    for i in range(1, length + 1):
        if x == i:
            continue
        if nums[x - 1][i - 1] != inf:
            print(x, i, nums[x - 1][i - 1], end= "")

        if (x == length and x == i + 1) or i == length:
            print()
        elif i < length:
            print(",", end= " ")