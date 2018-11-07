import requests
import time
import random

sleeptime = random.randint(0,2)+random.random()

print(sleeptime)
# time.sleep(sleeptime)
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# r = requests.get('http://www.santostang.com',headers=headers)
#
#
# print(r.request.headers)




# {'User-Agent': 'python-requests/2.19.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}