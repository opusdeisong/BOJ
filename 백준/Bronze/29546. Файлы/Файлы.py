n = int(input())

filenames = [input() for _ in range(n)]

m = int(input())

for _ in range(m):
    l, r = map(int, input().split())
    
    for i in range(l-1, r):
        print(filenames[i])
