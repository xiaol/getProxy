# -*- coding: utf-8 -*-
import time
import threading
from page import get_page

inFile = open('proxy.txt', 'r')
outFile = open('available.txt', 'w')

lock = threading.Lock()

def test():
    while True:
        lock.acquire()
        line = inFile.readline().strip()
        lock.release()
        if len(line) == 0: break
        protocol, proxy = line.split('=')
        d = {'protocol': protocol, 'proxy': proxy}
        try:
            text = get_page(url='https://www.baidu.com/', need_proxy=True, proxy=d)
            print text
            if u'把百度设为主页' in text:
                lock.acquire()
                print 'add proxy', proxy
                outFile.write(proxy + '\n')
                lock.release()
            else:
                print '.',
        except Exception, e:
            print e

all_thread = []
for i in range(50):
    t = threading.Thread(target=test)
    all_thread.append(t)
    t.start()
    
for t in all_thread:
    t.join()

inFile.close()
outFile.close()
