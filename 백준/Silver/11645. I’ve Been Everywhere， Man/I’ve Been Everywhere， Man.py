T = int(input())
for _ in range(T):
    n = int(input())
    list = []
    for i in range(n):
        temp = input()
        if temp not in list:
            list.append(temp)
    print(len(list))