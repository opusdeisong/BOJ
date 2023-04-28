a, b, c, d = map(int, input().split())
sum = a + b + c + d
aa, bb, cc, dd = map(int, input().split())
summ = aa + bb + cc + dd
ans = max(sum, summ)
print(ans)