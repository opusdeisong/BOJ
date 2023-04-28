import sys


a, b, c, d, e =1,2,3,4,5
aa, bb, cc, dd, ee= map(int, sys.stdin.readline().split())
big = 0
for i in range(16):
    for j in range(8):
        for k in range(6):
            for l in range(4):
                for m in range(4):
                    if (i + j + k + l + m) > 3:
                        if ((a * i + b * j + c * k + l * d + m * e) <= 15):
                            if ((aa * i + bb * j + cc * k + l * dd + m * ee) >= big):
                                big = (aa * i + bb * j + cc * k + l * dd + m * ee)
print(big)