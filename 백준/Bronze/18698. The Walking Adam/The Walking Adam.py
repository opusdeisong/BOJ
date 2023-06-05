import sys

T = int(sys.stdin.readline())
test_cases = []
for _ in range(T):
    test_cases.append(sys.stdin.readline().strip())
results = []
for case in test_cases:
    for i, step in enumerate(case):
        if step == 'D':
            results.append(i)
            break
    else:
        results.append(len(case))
for result in results:
    print(result)
