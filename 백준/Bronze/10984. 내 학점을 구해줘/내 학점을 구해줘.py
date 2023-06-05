import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_credits = 0
    total_score = 0.0
    for _ in range(N):
        C, G = map(float, sys.stdin.readline().split())
        total_credits += C
        total_score += C * G
    GPA = total_score / total_credits
    print(int(total_credits), round(GPA, 1))
