import sys

S = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

if S <= A:
    print(250)
elif (S - A) % B != 0:
    print(350 + ((S - A) // B) * 100)
else:
    print(250 + ((S - A) // B) * 100)