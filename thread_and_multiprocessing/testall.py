# -*- coding: utf-8 -*-

import threading

def func(lis,n):
    print('{} is print {} and {}'.format(threading.current_thread().name,lis,n))

def run():
    pool = []
    for lis,n in zip(range(10,20),range(40,50)):
        t = threading.Thread(target=func,args=(lis,n))
        pool.append(t)
    for t in pool:
        t.start()
    for t in pool:
        t.join()

run()

