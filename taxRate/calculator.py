#!/usr/bin/env python3
import sys
import os.path




class getinfo():
    def __init__(self):
        


def getPara():
    paral = []
    dic = {}
    for i in sys.argv[1:]:
        paral.append(i)
    
    for i in len(paral):
        if paral[i] == '-c':
            dic[cfg] = para[i+1]
        elif paral[i] == '-d':
            dic[icsv] = paral[i+1]
        elif paral[i] == '-o':
            dic[ocsv] = paral[i+1]
        else:
            print('Parameter Error')
            sys.exit(1) 
            
    for i in dic.values():
        if os.path.isfile(i):
            continue
        else:
            print('File Error')
            sys.exit(1)
    return dic


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
    dic1 = getpara()
