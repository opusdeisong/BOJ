import sys

T = int(sys.stdin.readline())
listt = [""]*100000

for _ in range(T):
    temp = input().split()
    listt[int(temp[1]) - 1] = temp[0][int(temp[2]) - 1]
for i in listt:
    if (i != ""):
        a = i
        a = a.upper()

        print(f"{a}", end="")

