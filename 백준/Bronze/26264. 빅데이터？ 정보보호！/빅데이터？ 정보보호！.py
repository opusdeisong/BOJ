import sys

N = int(sys.stdin.readline())
line = sys.stdin.readline()
ans = len(line) - 1
security = ans - 7 * N
bigdata = N - security
if security > bigdata:
    print("security!")
elif security < bigdata:
    print("bigdata?")
else:
    print("bigdata? security!")