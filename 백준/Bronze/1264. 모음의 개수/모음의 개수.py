import sys

while True:
    string = sys.stdin.readline()
    if string == '#\n': break
    list = []
    for i in string:
        list.append(i)
    num = 0
    num += list.count('a')
    num += list.count('e')
    num += list.count('i')
    num += list.count('o')
    num += list.count('u')
    num += list.count('A')
    num += list.count('E')
    num += list.count('I')
    num += list.count('O')
    num += list.count('U')
    print(num)