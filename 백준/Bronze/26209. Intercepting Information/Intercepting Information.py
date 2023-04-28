list = input().split()
flag = True
for i in list:
    if i != '0' and i != '1':
        flag = False
        break
if flag:
    print("S")
else:
    print("F")