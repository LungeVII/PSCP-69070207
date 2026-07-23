"""Divide 10"""

def main():
    """Divide 10"""
    nums = int(input())
    for i in reversed(range(0, nums+1)):
        if not i % 10 :
            print(i, end=" ")
main()
