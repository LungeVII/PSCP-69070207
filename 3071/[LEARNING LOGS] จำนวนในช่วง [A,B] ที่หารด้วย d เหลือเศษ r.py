"""kkk"""
A = int(input())
B = int(input())
d = int(input())
r = int(input())
List = []
for i in range(A,B+1):
    if i%d == r:
        List.append(i)
print(len(List))
