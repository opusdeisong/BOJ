import sys

def modular_exponentiation(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

test_cases = int(sys.stdin.readline())
for _ in range(test_cases):
    a, b = map(int, sys.stdin.readline().split())
    result = modular_exponentiation(a, b, 10)
    print(result if result != 0 else 10)
