import sys
list = []
x, b = map(int, sys.stdin.readline().split())
orig = x
if x < 0:
    x = -x
div = b
if orig > 0 and b < 0:
    while x != 0:
        r = x % b
        x = x // b
        if r < 0 and b < 0:
            r += abs(b)
            x -= b // abs(b)
        list.append(r)
else:
    while x != 0:
        temp = x % div
        list.append((x % div) / (div / b))
        x = x - temp
        div = div * b
list.reverse()
if orig == 0:
    print(0)
elif orig < 0 and b > 0:
    print("-",end="")
    for i in list:
        print(str(abs(int(i))),end="")
else:
    for i in list:
        print(str(abs(int(i))),end="")
