list = sorted(map(int, input().split()), reverse=True)
ans = sum(list[:2])
print(ans)