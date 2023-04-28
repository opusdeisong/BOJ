def make_list(a):
	list = []
	A = ""
	for i in range(len(a)):
		list.append(a[i])
	list.reverse()
	for i in list:
		A = A + i
	return int(A)
A, B = map(int, input().split())
a = str(A)
b = str(B)
A = make_list(a)
B = make_list(b)
if A > B:
	print(A)
else:
	print(B)