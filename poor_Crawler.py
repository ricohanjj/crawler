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
    Process_id = 'Process- '+index
