import sys
T = int(sys.stdin.readline())
for _ in range(T):
    yon = 0
    kor = 0
    for i in range(9):
        m, n = map(int,sys.stdin.readline().split())
        yon += m
        kor += n
    if yon == kor:
        print("Draw")
    elif yon > kor:
        print("Yonsei")
    else:
        print("Korea")
    continue