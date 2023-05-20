import sys

for _ in range(int(sys.stdin.readline())):
    ans = 0
    for __ in range(int(sys.stdin.readline())):
        temp = sys.stdin.readline().split()
        ans += int(temp[1]) * float(temp[2])
    print(f"${ans:.2f}")