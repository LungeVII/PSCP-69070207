"""kkkk"""
a = int(input())
b = int(input())
goal = int(input())

if a + (5 * b) < goal:
    print(-1)
else:
    use5_first = min(b, goal // 5)
    remain = goal - use5_first * 5

    if remain <= a:
        print(remain)
    else:
        print(-1)
