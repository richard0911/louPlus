#!/usr/bin/env python3
import sys
import os.path


class Info:
    def __init__(self):
        self.__salaryl = {}
        self.__configl = {}

    @property
    def salaryl(self):
        return self.__salaryl

    @salaryl.setter
    def salaryl(self, list1):
        self.__salaryl = list1

    @property
    def configl(self):
        return self.__configl

    @configl.setter
    def configl(self, list2):
        self.__configl = list2


def get_para():  # 从命令行参数获取输入信息
    paral = []
    dic = {}
    for i in sys.argv[1:]:
        paral.append(i)

    for i in range(len(paral)):
        if paral[i] == '-c':
            dic['cfg'] = paral[i+1]
        elif paral[i] == '-d':
            dic['icsv'] = paral[i+1]
        elif paral[i] == '-o':
            dic['ocsv'] = paral[i+1]

    for d in dic:
        if d == 'ocsv':
            continue
        if not os.path.exists(dic[d]):
            print('file not exists')
            sys.exit(1)
    return dic


def read_file(filename):  # 读取文件
    listt = []
    with open(filename) as file:
        for i in file:
            if i == '\n':
                break
            if '=' in i:
                opera = '='
            else:
                opera = ','
            try:
                i, j = i.strip().split(opera)
            except:
                print('File Error')
            listt.append([i.strip(), float(j.strip())])
        dic = dict(listt)
    return dic


def write_file(filename, dic):  # 写入文件
    with open(filename, 'w') as file:
        for d in dic:
            s = '{},{},{:.2f},{:.2f},{:.2f}\n'.format(d, int(dic[d][0])
                                          , dic[d][1], dic[d][2]
                                          , dic[d][3])
            file.write(s)


def cal(dc, ds):
    dic = {}
    JiShuL = dc['JiShuL']
    JiShuH = dc['JiShuH']
    insurespre = dc['YangLao'] + dc['YiLiao'] + dc['ShiYe'] + dc['GongShang'] + dc['ShengYu'] + dc['GongJiJin']

    for i in ds:
        salary = ds[i]
        if salary > JiShuH:
            insures = JiShuH * insurespre
        elif salary < JiShuL:
            insures = JiShuL * insurespre
        else:
            insures = salary * insurespre

        tax = salary - insures

        if tax <= 1500:
            tax = tax * 0.03 - 0
        elif tax <= 4500:
            tax = tax * 0.10 - 105
        elif tax <= 9000:
            tax = tax * 0.20 - 555
        elif tax <= 35000:
            tax = tax * 0.25 - 1005
        elif tax <= 55000:
            tax = tax * 0.30 - 2755
        elif tax <= 80000:
            tax = tax * 0.35 - 5505
        else:
            tax = tax * 0.45 - 13505

        after = salary - insures - tax
        list1 = [salary, insures, tax, after]
        dic[i] = list1

    return dic

if __name__ == '__main__':
    dic1 = get_para()
    cl = Info()
    cl.salaryl = read_file(dic1['icsv'])
    cl.configl = read_file(dic1['cfg'])
    dic2 = cal(cl.configl, cl.salaryl)
    write_file(dic1['ocsv'], dic2)
