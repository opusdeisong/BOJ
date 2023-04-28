N = int(input())
num = []
for i in range(N):
    new = int(input())
    if new == 0:
        num.pop()
    else:
        num.append(new)
print(sum(num))