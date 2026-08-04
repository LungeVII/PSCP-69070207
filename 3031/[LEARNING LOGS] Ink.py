"""time to kill by sqiud"""
import math
def main():
    """time to kill by sqiud"""
    S, N = map(int, input().split())
    for i in range(N):
        i = i+1
        x,y = map(int, input().split())
        radius = math.sqrt((x)**2+y**2)
        time = ((radius**2)*(3.1416))/S
        print(math.ceil(time))
main()
