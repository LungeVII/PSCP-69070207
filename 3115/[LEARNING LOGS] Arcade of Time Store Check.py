"""Store Check"""

def main():
    """Calculate Time to Close"""
    Number_of_stores, check_time = map(int, input().split())
    List1 = []
    List2 = []
    check_time += 1
    for _ in range(Number_of_stores):
        start, stop = map(int, input().split())
        for k in range(start, stop):
            List1.append(k) #ผมไม่รู้ว่างจะเช็คค่าระหว่างยังไงก็เลยมันสะทุกค่าเลย

    List2 = list(map(int, input().split()))

    for k in List2:
        y = List1.count(k)
        print(y, end=" ")

main()
