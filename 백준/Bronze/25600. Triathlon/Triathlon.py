max_ = 0
T = int(input())
for _ in range(T) :
    a, d, g = map(int, input().split())
    if a == d + g :
        temp = a * (d + g) * 2
    else :
        temp = a * (d + g)
    max_ = max(temp, max_)

print(max_)