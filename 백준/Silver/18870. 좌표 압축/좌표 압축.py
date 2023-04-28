import sys
T = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
new_list = num.copy()
dic = {}
j = 0
new_list.sort()
for i in new_list:
    if i not in dic:
        dic[i] = j
        j += 1
for i in num:
    print(f"{dic[i]}",end= " ")