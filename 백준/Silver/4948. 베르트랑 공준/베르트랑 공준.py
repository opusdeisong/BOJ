from math import sqrt

N = 123456 * 2 + 1
num = [True] * N
for i in range(2, int(sqrt(N)) + 1):
	if num[i]:
		for j in range(2 * i, N, i):
			num[j] = False

while True:
	a = int(input())
	if a == 0:
		break
	cnt = 0
	for i in range(a + 1, a * 2 + 1):
		if num[i]:
			cnt += 1
	print(cnt)