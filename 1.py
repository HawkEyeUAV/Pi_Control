#!/usr/bin/env python3

import time
from multiprocessing import Pool,Manager,Queue

q = Manager().Queue()
for i in range(11):
    q.put(i)

def A(i):
    num = q.get_nowait()
    print('ddd:%d'%(num))
    time.sleep(1)
            

pool = Pool(3)

for i in range(10):
    pool.apply_async(A,(i,))

pool.close()
pool.join()
