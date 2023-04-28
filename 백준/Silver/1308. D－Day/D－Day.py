Y, M, D = map(int, input().split())
YY, MM, DD = map(int, input().split())

import datetime

d_day = int(str(datetime.date(YY, MM, DD)-datetime.date(Y, M, D)).split()[0])

over = 0
for i in range(0,1000) :
    if i % 400==0 :
        over +=366
    elif i % 100==0 :
        over += 365
    elif i % 4==0 :
        over += 366
    else :
        over += 365

if d_day >= over :
    print('gg')
else :
    print(f'D-{d_day}')