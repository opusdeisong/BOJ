import sys
T = int(sys.stdin.readline())
num = sys.stdin.readline().split()
ans = input()
cnt = 0
for i in num:
    if i == ans:
        cnt += 1
        
print(cnt)