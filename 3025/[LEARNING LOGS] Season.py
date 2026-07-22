"""kkk"""
x = int(input())  # month
y = int(input())  # day

if x in (1,2):
    print("winter")
elif x == 3:
    if y < 21:
        print("winter")
    else:
        print("spring")
elif x in (4,5):
    print("spring")
elif x == 6:
    if y < 21:
        print("spring")
    else:
        print("summer")
elif x in (7,8):
    print("summer")
elif x == 9:
    if y < 21:
        print("summer")
    else:
        print("fall")
elif x in (10,11):
    print("fall")
elif x == 12:
    if y < 21:
        print("fall")
    else:
        print("winter")
