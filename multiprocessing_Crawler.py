from multiprocessing import cpu_count
from multiprocessing import Process,Queue
import time
import requests
import os
#print(cpu_count())

link_list = []
with open("alexa.txt",'r') as f:
    url_lists = f.readlines()
    for eachone in url_lists:
        url_temp = eachone.split('\t')[1]
        url = url_temp.replace('\n','')
        link_list.append(url)

class MyProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q = q
    def run(self):
        print('starting：',self.pid)
        time.sleep(3)
        while not self.q.empty():
            time.sleep(1)
            crawler(self.q)
        print('Exiting...',self.pid)

def crawler(q):
    url = q.get(timeout=20)
    try:
        r = requests.get(url,timeout=20)
        print(q.qsize(),url,r.status_code,os.getpid())
    except Exception as e:
        print(q.qsize(),url,'Error: ',e)

if __name__=='__main__':
    Processlists = []
    workQueue = Queue(300)
    for url in link_list:
        workQueue.put(url)
    start = time.time()
    for i in range(0,3):
        p = MyProcess(workQueue)
        p.daemon = True
        p.start()
        Processlists.append(p)
    for i in Processlists:
        i.join()
    # time.sleep(10)
    end = time.time()
    print('using ',end-start)
    print('Main Process exit')

