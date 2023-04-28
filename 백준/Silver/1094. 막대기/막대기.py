def find_stick(X):
    if X in list:
        return 1
    else:
        for i in range(len(list)):
            if X < list[i]:
                temp = i
                break
        return find_stick(X - list[i - 1]) + 1

X = int(input())
list = [1, 2, 4, 8, 16 ,32 ,64]
print(find_stick(X))