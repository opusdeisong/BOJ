import sys


def will_sticker_fit(wc, hc, ws, hs):
    if (wc - ws >= 2) and (hc - hs >= 2):
        return 1
    else:
        return 0

wc, hc, ws, hs = map(int, sys.stdin.readline().split())
print(will_sticker_fit(wc, hc, ws, hs))
