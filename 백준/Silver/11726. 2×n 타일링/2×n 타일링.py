import sys

n = int(sys.stdin.readline())
s = [0, 1, 2]
for i in range(3, n + 1):
  s.append(s[i - 2] + s[i - 1])
print(s[n] % 10007)