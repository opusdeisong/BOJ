n, h, v = map(int, input().split())
ans = max(h, n-h) * max(v, n-v)
print(ans * 4)