import sys
from string import ascii_uppercase


while True:
    comm = sys.stdin.readline().rstrip()
    alphabet = list(ascii_uppercase)
    if comm == "R0C0":
        break
    comm = comm[1:]
    num, alph = map(int, comm.split("C"))
    alph -= 1
    ans = ""
    while alph >= 0:
        temp = alph % 26
        alph = alph // 26 - 1
        ans = alphabet[temp] + ans
    print(f"{ans}{num}")