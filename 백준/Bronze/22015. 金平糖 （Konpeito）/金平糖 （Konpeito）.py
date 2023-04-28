A, B, C = map(int, input().split())

ans = max([A, B, C]) * 3 - sum([A, B, C])
print(ans)