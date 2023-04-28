T = int(input())
pro = 0
cons = 0

for i in range(T):
    N = int(input())
    if N == 1:
        pro += 1
    else:
        cons += 1
if pro > cons:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")