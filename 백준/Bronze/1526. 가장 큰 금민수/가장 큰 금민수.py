n = int(input())
list = []
for i in range(n + 1):
    flag = True
    for j in str(i):
        if j != '4' and j != '7':
            flag = False
    if flag:
        list.append(i)

print(list[-1])