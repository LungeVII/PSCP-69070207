"""[LEARNING LOGS] สลากกินแบ่ง"""

def main():
    """main"""
    char, num = input().split()
    buy_char, buy_num = input().split()
    reward = 0

    if char == buy_char and num == buy_num:
        reward = 1000000

    elif char != buy_char and num == buy_num:
        reward = 100000

    elif char == buy_char:
        if int(num[-3:]) == int(buy_num[-3:]):
            reward = 2000
        elif int(num[-2:]) == int(buy_num[-2:]):
            reward = 1000
        else:
            reward = 20

    elif char != buy_char:
        if int(num[-3:]) == int(buy_num[-3:]):
            reward = 200
        elif int(num[-2:]) == int(buy_num[-2:]):
            reward = 100

    print(reward)

main()
