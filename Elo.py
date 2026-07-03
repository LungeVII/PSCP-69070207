"""kkk"""
import math
ra = int(input())
rb = int(input())
x = input()

ea = 1/1+(10**((rb-ra)/400))
eb = 1/1+(10**((ra-rb)/400))

if x == "A" :
    print(1-ea)
elif x == "B" :
    print(1-eb)
