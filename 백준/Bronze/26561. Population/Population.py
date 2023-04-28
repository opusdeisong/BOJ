T = int(input())

for _ in range(T):
    p, t = map(int, input().split())
    d = t // 7
    b = t // 4
    print(p - d + b)