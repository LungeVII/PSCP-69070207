"""kkk"""
N, S = map(int, input().split())
number = []

for _ in range(N):
    number.append(int(input()))

count = 0
seen = []

for _ in range(N):
    if not S or S in seen:
        break

    seen.append(S)
    count += 1
    S = number[S - 1]

print(count)
