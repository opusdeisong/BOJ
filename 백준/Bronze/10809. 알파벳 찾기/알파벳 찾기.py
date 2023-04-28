S = input()
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for j in alph:
	for i in range(len(S)):
		if j == S[i]:
			print(i,end=" ")
			break
		if i == len(S) - 1:
			print(-1, end = " ")