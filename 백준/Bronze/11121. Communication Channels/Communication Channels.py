import sys

T = int(sys.stdin.readline())

for _ in range(T):
    input_string, output_string = sys.stdin.readline().split()

    if input_string == output_string:
        print('OK')
    else:
        print('ERROR')
