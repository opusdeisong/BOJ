import sys

N = int(sys.stdin.readline())
ans = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#for i in range(200, 240):
#    print(f"{i}레벨이면 {ans[i % 200]}")
print(ans[N % 200])