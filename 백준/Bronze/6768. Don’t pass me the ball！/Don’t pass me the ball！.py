import sys

J = int(sys.stdin.readline())
cnt = 0
for i in range(1, J):
    for j in range(i+1, J):
        for k in range(j+1, J):
            cnt += 1
print(cnt)
