import sys


ds, ys = map(int, sys.stdin.readline().split())
dm, ym = map(int, sys.stdin.readline().split())
next_sun = - ds + ys
next_moon = - dm + ym

while next_sun != next_moon:
    if next_sun < next_moon:
        next_sun += ys
    else:
        next_moon += ym


print(next_sun)
