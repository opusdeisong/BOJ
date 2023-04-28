import sys

n = int(sys.stdin.readline())

def power(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        return power(solution(a, a), b // 2)
    else:
        return solution(power(a, b - 1), a)

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(2):
                sum += arr1[i][k] * arr2[k][j]
            answer[i][j] = sum % 1000000007
    return answer
tempp = [[1,1],[1,0]]
start = [[1],[1]]

if n < 3:
    print(1)
else:
    print(solution(power(tempp, n - 2), start)[0][0])