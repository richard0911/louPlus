#!/usr/bin/env python3
import sys

try:
    price = int(sys.argv[1])
except:
    print('Parameter Error')


def cal(price):
    amount = price - 3500 
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
    print('{:.2f}'.format(amount))


if __name__ == '__main__':
    cal(price)
