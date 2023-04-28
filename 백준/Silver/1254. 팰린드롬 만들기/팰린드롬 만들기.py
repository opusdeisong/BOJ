list = input()

for i in range(len(list)):
    if list[i:] == list[i:][::-1]:
        print(len(list) + i)
        break