"""kkk"""
def main():
    """kkk"""
    N, K, T = map(int, input().split())

    if T == 1:
        print(1)
        return

    person = 1
    count = 1

    while True:
        person = (person - 1 + K) % N + 1

        if person == T:
            count += 1
            break

        if person == 1:
            break

        count += 1

    print(count)


main()
