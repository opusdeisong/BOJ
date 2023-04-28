import math
N = int(input())
Set = []
for i in str(N):
    if i != "0":
        Set.append(int(i))
Set = list(set(Set))
for i in range(1, len(Set)):
    Set[0] = math.lcm(Set[0], Set[i])
k = Set[0]
if N % k == 0:
    print(N)
else:
    cnt = 1
    check = 0
    while True:
        for i in range(0, 10 ** cnt):
            if int(str(N) + "0" * (cnt - len(str(i))) + str(i)) % k == 0:
                print(int(str(N) + "0" * (cnt - len(str(i))) + str(i)))
                check = 1
                break
        if check == 1:
            break
        cnt += 1