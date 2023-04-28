t = int(input())

for _ in range(t):
    Lt, Wt, Le, We = map(int, input().split())
    if Lt * Wt > Le * We :
        print("TelecomParisTech")
    elif Lt * Wt < Le * We :
        print("Eurecom")
    else :
        print("Tie")