from multiprocessing import Pool,Manager
import time
import requests

link_list = []
with open("alexa.txt",'r') as f:
    url_lists = f.readlines()
    for eachone in url_lists:
        url_temp = eachone.split('\t')[1]
        url = url_temp.replace('\n','')
        link_list.append(url)

start = time.time()
def crawler(q,index):
    Process_id = 'Process- '+str(index)
    while not q.empty():
        url = q.get(timeout=20)
        try:
            r = requests.get(url,timeout=20)
            print(Process_id,q.qsize(),r.status_code,url)
        except Exception as e:
            print(Process_id,q.qsize(),url,'Error:',e)

if __name__ == '__main__':
    manager = Manager()
    workQueue = manager.Queue(1000)

    for url in link_list:
        workQueue.put(url)

    pool = Pool(processes=3)
    for i in range(4):
        # print(i)
        pool.apply_async(crawler,args=(workQueue,i))
    #
    print("Start Processes")
    pool.close()
    pool.join()

    print('Main Process quit')



