import sys

N = int(sys.stdin.readline())
print("int a;")
for i in range(1, N+1):
    if i == 1:
        print("int *ptr = &a;")
    else:
        print("int " + "*" * i + "ptr" + str(i if i != 1 else "") + " = &" + ("ptr" + str(i-1 if i-1 != 1 else "")) + ";")
