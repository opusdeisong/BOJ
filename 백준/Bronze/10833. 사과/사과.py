N = int(input())
remain_apple = 0
for _ in range(N):
    students, apples = map(int, input().split())
    remain_apple += apples % students
print(remain_apple)
