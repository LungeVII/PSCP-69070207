"""kkk"""

T = int(input())

for _ in range(T):

    N = int(input())

    LIST = []

    for _ in range(N):
        x, y = map(int, input().split())
        LIST.append([x, y])

    DATA = []

    for point in LIST:
        x = point[0]
        y = point[1]
        DATA.append([x + y, -y, x, y])

    DATA.sort()

    for point in DATA:
        print(point[2], point[3])
