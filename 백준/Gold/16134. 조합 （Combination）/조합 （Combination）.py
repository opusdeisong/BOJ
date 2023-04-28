def comb(N, R):
    if R == 0 or N == R:
        return 1

    else:
        return comb(N - 1, R - 1) + comb(N - 1, R)

N, R = map(int, input().split())

print(comb(N, R) % 1000000007)

