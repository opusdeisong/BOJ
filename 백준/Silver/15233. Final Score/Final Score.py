A, B, G = map(int, input().split())
A_l = input().split()
B_l = input().split()
G_l = input().split()
A_s = 0
for i in A_l:
    A_s += G_l.count(i)
B_s = 0
for i in B_l:
    B_s += G_l.count(i)

if A_s > B_s:
    print("A")
elif A_s < B_s:
    print("B")
else:
    print("TIE")