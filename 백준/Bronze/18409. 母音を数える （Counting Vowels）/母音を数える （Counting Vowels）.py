n=int(input())
arr=['a', 'e', 'i', 'o', 'u']
name = input()
ans=0
for i in name:
    if i in arr:
        ans += 1
print(ans)