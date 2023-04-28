import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = {}

for i in range(N):
    site_name, password = input().split()
    add[site_name] = password

for i in range(M):
    print(add[input().rstrip()])