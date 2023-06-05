t = int(input())

for _ in range(t):
    first, second = map(int, input().split(' '))

    festival1_prize = 0
    if first == 1:
        festival1_prize = 5000000
    elif 1 < first <= 3:
        festival1_prize = 3000000
    elif 3 < first <= 6:
        festival1_prize = 2000000
    elif 6 < first <= 10:
        festival1_prize = 500000
    elif 10 < first <= 15:
        festival1_prize = 300000
    elif 15 < first <= 21:
        festival1_prize = 100000

    festival2_prize = 0
    if second == 1:
        festival2_prize = 5120000
    elif 1 < second <= 3:
        festival2_prize = 2560000
    elif 3 < second <= 7:
        festival2_prize = 1280000
    elif 7 < second <= 15:
        festival2_prize = 640000
    elif 15 < second <= 31:
        festival2_prize = 320000

    total_prize = festival1_prize + festival2_prize
    print(total_prize)
