"""kkk"""

N, P = map(int, input().split())
P = float(P)


LIST = []

for i in range(N):
    row = list(map(int, input().split()))
    LIST.append(row)

check1 = []
check2 = []
check3 = []
check4 = []

for j in LIST:
    check2.append(sum(j))


for j in LIST:
    count = 0
    for i in j:
        if i > 0:
            count += 1
    check1.append(count)


for j in range(N):
    count = 0
    total = 0
    for i in range(N):
        if LIST[i][j] > 0:
            count += 1

        if LIST[i][j] > 0:
            total += LIST[i][j]
    check3.append(count)
    check4.append(total)

for i in range(N):
    print(*LIST[i],check1[i],check2[i])
print(*check3)
print(*check4)
print(sum(check3), sum(check4), f"{sum(check4)*P:.2f}")
