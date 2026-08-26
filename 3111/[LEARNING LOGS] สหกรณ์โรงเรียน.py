"""Store of School"""
import math
def main():
    """Store of School"""
    char = input().upper()
    things = int(input())
    total = 0
    for _ in range(things):
        price = float(input())
        total += price

    if char == "Y":
        total *= 0.95
        print(f"{math.ceil(total*100)/100:.2f}")
    elif char == "N":
        if total >= 500:
            total *= 0.97
            print(f"{math.ceil(total*100)/100:.2f}")
        else:
            print(f"{math.ceil(total*100)/100:.2f}")
main()
