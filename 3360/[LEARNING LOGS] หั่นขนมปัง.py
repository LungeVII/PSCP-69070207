"""kkk"""

W, H, M, N = map(int, input().split())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

X.insert(0, 0)
Y.insert(0, 0)

X.append(W)
Y.append(H)

width = []
height = []

for i in range(M + 1):
    x = X[i+1] - X[i]
    width.append(x)

for i in range(N + 1):
    y = Y[i+1] - Y[i]
    height.append(y)

x2 = sorted(width)
y2 = sorted(height)

highest = max(width) * max(height)

higher = max(
    x2[-2] * max(height),
    max(width) * y2[-2]
)

print(f"{highest} {higher}")
