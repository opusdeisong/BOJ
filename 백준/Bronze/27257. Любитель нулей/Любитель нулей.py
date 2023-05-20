import sys

k = int(sys.stdin.readline())
k_str = str(k)
k_str = k_str.rstrip('0')
beauty = k_str.count('0')

print(beauty)
