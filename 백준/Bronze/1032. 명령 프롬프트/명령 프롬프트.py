N = int(input())
name = list(input())
for i in range(N - 1):
    temp = list(input())
    for j in range(len(name)):
        if name[j] != temp[j]:
            name[j] = '?'
print(''.join(name))