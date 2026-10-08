"""kkk"""
n = int(input())

giraffe = []

for i in range(n):
    giraffe.append(int(input()))

count = 0

for i in range(n):

    # มีแค่ 1 ตัว
    if n == 1:
        count += 1

    # ตัวแรก
    elif not i:
        if giraffe[i] > giraffe[i + 1]:
            count += 1

    # ตัวสุดท้าย
    elif i == n - 1:
        if giraffe[i] > giraffe[i - 1]:
            count += 1

    # ตัวตรงกลาง
    else:
        if giraffe[i] > giraffe[i - 1] and giraffe[i] > giraffe[i + 1]:
            count += 1

print(count)
