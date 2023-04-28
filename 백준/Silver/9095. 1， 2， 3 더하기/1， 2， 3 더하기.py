import sys
def find_ans(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return find_ans(N - 3) + find_ans(N - 2) + find_ans(N - 1)

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    print(find_ans(N))