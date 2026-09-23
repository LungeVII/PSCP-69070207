"""kkk"""
L, N = map(int, input().split())

band = 1
count = L * (L + 1) // 2

while N > count:
    N -= count
    band += 1
    count += L * L

print(band)
