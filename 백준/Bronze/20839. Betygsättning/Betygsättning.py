import sys

x, y, z = map(int, sys.stdin.readline().split())
xp, yp, zp = map(int, sys.stdin.readline().split())

if xp == x and yp == y and zp == z:
    print('A')
elif yp == y and zp == z and xp >= x/2:
    print('B')
elif yp == y and zp == z:
    print('C')
elif zp == z and yp >= y/2:
    print('D')
elif zp == z:
    print('E')
