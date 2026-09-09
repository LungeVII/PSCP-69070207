"""[LEARNING LOGS] กบน้อยกระโดด"""

def main():
    """main"""

    x,y = map(int, input().split())
    total = 0
    count = 0

    for i in range(x,0,-2):
        total += i
        count += 1
        if total >= y:
            break


    if total >= y:
        print(count)
    else:
        print(-1)

main()
