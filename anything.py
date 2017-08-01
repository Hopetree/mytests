# -*- coding: utf-8 -*-

# 多进程测试

from multiprocessing import Pool
import os, time, random


def long_time_task(sr):
    print('{} is running,num is {}'.format(os.getpid(),sr))
    time.sleep(1)

def main():
    p = Pool()
    p.map_async(long_time_task, list(range(20)))
    p.close()
    p.join()


if __name__=='__main__':
    t = time.time()
    main()
    print('%0.2f'%float(time.time()-t))