N, X = map(int, input().split())
A = list(map(int, input().split()))

sum_prices = [A[i] + A[i + 1] for i in range(N - 1)]

min_cost = min(sum_prices) * X

print(min_cost)
