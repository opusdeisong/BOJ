N = int(input())
T = input()
a = 0
b = 0
for i in T:
    if i == "A":
        a += 1
    elif i == "B":
        b += 1
if a == b:
    print("Tie")
elif a > b:
    print("A")
elif a < b:
    print("B")