import sys


def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

T = int(sys.stdin.readline())
for _ in range(T):
    ans = 0
    temp = int(sys.stdin.readline())
    for i in range(2, temp // 2 + 1):
        if (check_prime(i)):
            if check_prime(temp - i):
                ans = 1
                break
    if ans == 1:
        print("Yes")
        continue
    else:
        print("No")