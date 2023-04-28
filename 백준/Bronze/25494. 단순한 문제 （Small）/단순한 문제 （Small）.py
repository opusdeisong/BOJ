T = int(input())
while T > 0:
    T = T - 1
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))