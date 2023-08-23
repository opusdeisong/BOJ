a = input()
b = input()
result = []

for digit_a, digit_b in zip(a, b):
    result.append(max(digit_a, digit_b))

print(''.join(result))
