T = int(input())

temp = list(map(int, input().split()))
temp.sort()
print(temp[0] * temp[-1])