import sys

enc = sys.stdin.readline().rstrip()
dec = enc[0]
temp = ord(enc[0]) - ord('A') + 1
while(temp < len(enc) - 1):
    dec += enc[temp]
    temp += ord(enc[temp]) - ord('A') + 1
dec += enc[-1]
print(dec)