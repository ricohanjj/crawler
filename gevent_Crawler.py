import gevent
import time
import requests
from gevent.queue import Queue,Empty
from gevent import monkey
monkey.patch_all()

link_list = []
with open("alexa.txt",'r') as f:
    url_lists = f.readlines()
    for eachone in url_lists:
        url_temp = eachone.split('\t')[1]
        url = url_temp.replace('\n','')
        link_list.append(url)


def crawler(index):
    Process_id = 'Process- ' + str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout=20)
        try:
            r = requests.get(url,timeout=20)
            print(Process_id,workQueue.qsize(),url,r.status_code)
        except Exception as e:
            print(Process_id,workQueue.qsize(),url,'Error',e)

if __name__=='__main__':
    workQueue = Queue(1000)
    for url in link_list:
        workQueue.put_nowait(url)
    jobs =[]
    for i in range(10):
        jobs.append(gevent.spawn(crawler,i))
    gevent.joinall(jobs)

# from gevent import monkey
# monkey.patch_all()
# import gevent
# import requests
#
# def f(url):
#     print('GET: %s' % url)
#     resp = requests.get(url)
#     data = resp.text
#     print(len(data))
#
# gevent.joinall([
#     gevent.spawn(f, 'https://www.python.org/'),
#     gevent.spawn(f, 'https://www.yahoo.com/'),
#     gevent.spawn(f, 'https://github.com/'),])


