"""kkk"""

num = int(input())
total = 0
for i in range(num):
    i += 1
    symbol = input()
    if symbol == "+":
        total += 10
    else:
        total -= 5
print(total)
