N, I = map(int, input().split())
list = [0 for i in range(N)]
for i in range(N):
    list[i] = input()
list.sort()
print(list[I - 1])