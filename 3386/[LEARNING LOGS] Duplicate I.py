"""kkkk"""

m = int(input())
n = int(input())

x = []
y = []
z = []

for _ in range(m):
    x.append(int(input()))

for _ in range(n):
    y.append(int(input()))

for a in x:
    for b in y:
        if a == b:
            z.append(a)
        else:
            pass

z.sort()

if z:
    for u in reversed(z):
        print(f"{u}")
else:
    print("Nope")
