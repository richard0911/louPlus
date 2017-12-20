#!/usr/bin/env python3
import sys
import os.path
from multiprocessing import Queue, Process
import getopt
from datetime import datetime
import configparser


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
    dic = {}
    argv = sys.argv[1:]
    shortargs = 'hC:c:d:o:'
    longargs = ['help']

    opts, args = getopt.getopt(argv, shortargs, longargs)

    for key, val in opts:
        if key == '-C':
            dic['city'] = val.upper()
        elif key == '-c':
            dic['config'] = val
        elif key == '-d':
            dic['info'] = val
        elif key == '-o':
            dic['output'] = val
        elif key in ('-h', '--help'):
            print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
            exit(0)
        else:
            print('args Error')
            exit(0)

    for d in dic:
        if d == 'output' or d == 'city':
            continue
        if not os.path.exists(dic[d]):
            print('files not exists')
            sys.exit(1)

    return dic


def read_file_c(filename, city=''):  # 读取文件
    listt = []
    if city == '':
        city = 'DEFAULT'
    with open(filename) as file:
        config = configparser.ConfigParser(allow_no_value=True)
        config.read_file(file)
        cof = config[city].keys()
        for i in cof:
            listt.append([i, config[city][i]])
        dic = dict(listt)

    return dic


def read_file(filename):  # 读取文件
    listt = []
    with open(filename) as file:
        for i in file:
            if i == '\n':
                break
            try:
                i, j = i.strip().split(',')
            except:
                print('File Error')
            listt.append([i.strip(), j.strip()])
        dic = dict(listt)
    return dic


def write_file(filename, dic):  # 写入文件
    with open(filename, 'w') as file:
        for d in dic:
            s = '{},{},{:.2f},{:.2f},{:.2f},{}\n'.format(d, int(dic[d][0]),
                                                         dic[d][1], dic[d][2],
                                                         dic[d][3], dic[d][4])
            file.write(s)


def cal(dc, ds):
    dic = {}
    jishul = float(dc['jishul'])
    jishuh = float(dc['jishuh'])
    insurespre = float(dc['yanglao']) + float(dc['yiliao']) + \
                 float(dc['shiye']) + float(dc['gongshang']) + \
                 float(dc['shengyu']) + float(dc['gongjijin'])

    for i in ds:
        salary = float(ds[i])
        if salary > jishuh:
            insures = jishuh * insurespre
        elif salary < jishul:
            insures = jishul * insurespre
        else:
            insures = salary * insurespre

        tax = salary - insures - 3500

        if tax <= 0:
            tax = 0
        elif tax <= 1500:
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
        now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        list1 = [salary, insures, tax, after, now]
        dic[i] = list1

    return dic


def part1():
    dic1 = get_para()
    cl = Info()
    cl.salaryl = read_file(dic1['info'])
    cl.configl = read_file_c(dic1['config'], dic1['city'])
    package = [cl, dic1]
    queue1.put(package)


def part2():
    package = queue1.get()
    cl = package[0]
    dic2 = cal(cl.configl, cl.salaryl)
    package.append(dic2)
    queue2.put(package)


def part3():
    package = queue2.get()
    dic1, dic2 = package[1], package[2]
    write_file(dic1['output'], dic2)


if __name__ == '__main__':
    queue1 = Queue()
    queue2 = Queue()
    proc1 = Process(target=part1)
    proc2 = Process(target=part2)
    proc3 = Process(target=part3)
    proc1.start()
    proc2.start()
    proc3.start()


