# -*- coding: utf-8 -*-

import multiprocessing as mp

def func(n):
    for i in range(n):
        print(i)

if __name__ == '__main__':
    lis = list(range(10))
    p = mp.Pool()
    p.map_async(func,lis)
    p.close()
    p.join()
