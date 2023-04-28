from math import sqrt
T = int(input())
for i in range(T):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	dis = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
	if dis == 0 and r1 == r2:
		print(-1)
	elif r1 + r2 == dis or abs(r1 - r2) == dis:
		print(1)
	elif abs(r1 - r2) < dis and abs(r1 + r2) > dis:
		print(2)
	else:
		print(0)