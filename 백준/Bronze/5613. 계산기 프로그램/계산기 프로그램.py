import sys

result = int(sys.stdin.readline())
operator = ''

while operator != '=':
    operator = sys.stdin.readline().strip()
    if operator == '=':
        break
    number = int(sys.stdin.readline())

    if operator == '+':
        result += number
    elif operator == '-':
        result -= number
    elif operator == '*':
        result *= number
    elif operator == '/':
        result //= number

print(result)
