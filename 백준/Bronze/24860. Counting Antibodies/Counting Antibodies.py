import sys

vk, jk = map(int, sys.stdin.readline().split())
vl, jl = map(int, sys.stdin.readline().split())
vh, dh, jh = map(int, sys.stdin.readline().split())

k = vk * jk
l = vl * jl
h = vh * dh * jh

ans = k * h + l * h

print(ans)
