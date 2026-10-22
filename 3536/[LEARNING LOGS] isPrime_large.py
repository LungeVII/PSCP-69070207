
"""kkk"""

n = int(input())

if n <= 1:
    print("NO")
elif n == 2:
    print("YES")
elif not n % 2 :
    print("NO")
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if not n % i :
            print("NO")
            break
    else:
        print("YES")
