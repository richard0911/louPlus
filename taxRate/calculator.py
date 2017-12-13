#!/usr/bin/env python3
import sys

def getPara():
    wages = []
    for i in sys.argv[1:]:
        try:
            info = [int(i.split(':')[0]), int(i.split(':')[1])]
        except:
            print('Parameter Error')
            sys.exit(0)
        wages.append(info)
    return wages


def cal(price):
    for wid in wages:
        wage = wid[1]
        insures = wage * 0.165
        amount = wage - 3500 - insures
        after = 0
        if amount > 0:
            if amount <= 1500:
                amount = amount * 0.03 - 0
            elif amount <= 4500:
                amount = amount * 0.10 - 105
            elif amount <= 9000:
                amount = amount * 0.20 - 555
            elif amount <= 35000:
                amount = amount * 0.25 - 1005
            elif amount <= 55000:
                amount = amount * 0.30 - 2755
            elif amount <= 80000:
                amount = amount * 0.35 - 5505
            else:
                amount = amount * 0.45 - 13505
            after = wage - insures - amount
        else:
            after = wage - insures
        print('{}:{:.2f}'.format(wid[0], after))


if __name__ == '__main__':
    wages = getPara()
    cal(wages)
