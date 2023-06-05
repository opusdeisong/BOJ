import sys

N = int(sys.stdin.readline())
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    candidate_number = data[0]
    scores = data[1:]
    total = sum(scores)
    if total < 55:
        print(f'{candidate_number} {total} FAIL')
        continue
    for i in range(3):
        if scores[i] < [35, 25, 40][i] * 0.3:
            print(f'{candidate_number} {total} FAIL')
            break
    else:
        print(f'{candidate_number} {total} PASS')
