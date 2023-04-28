import sys
from collections import Counter
N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))
print(round(sum(num) / N))

num.sort()

print(num[N // 2])

new_num = Counter(num).most_common()

if len(num) > 1:
    if new_num[0][1] == new_num[1][1]:
        print(new_num[1][0])
    else:
        print(new_num[0][0])
else:
    print(num[0])

print(num[-1] - num[0])
