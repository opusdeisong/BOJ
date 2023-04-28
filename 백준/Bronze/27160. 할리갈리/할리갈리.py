import sys
N = int(sys.stdin.readline())
list =[0, 0, 0, 0]
for i in range(N):
    a, b = sys.stdin.readline().split()
    if a == "BANANA":
        list[0] += int(b)
    elif a == "STRAWBERRY":
        list[1] += int(b)
    elif a == "LIME":
        list[2] += int(b)
    elif a == "PLUM":
        list[3] += int(b)
if 5 in list:
    print("YES")
else:
    print("NO")