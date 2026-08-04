"""Min of break the door"""
import math

num = int(input())

if num == 1:
    print(0)
elif num == 3:
    print(1)
elif num in (2,4):
    print(2)
else:
    row = math.ceil(math.sqrt(num))

    if row%2  and num % 2 :
        print(row//2 * 4)
    elif row % 2  and not num % 2:
        print((row//2 * 4)-1)
    elif not row % 2 and num % 2  and not row % 4:
        print((row//2 * 2)+1)
    elif not row % 2 and num % 2  and not row % 6:
        print((row//2 * 3))
    elif not row % 2 and not num % 2 and not row % 2:
        print((row-1)*2)
