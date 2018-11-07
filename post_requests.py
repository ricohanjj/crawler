import requests
import http.cookiejar
session = requests.session()

post_url=r'http://www.santostang.com/wp-login.php'
agent =r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
headers = {
    "Host":"www.santostang.com",
    "Origin":"http://www.santostang.com",
    "Referer":"http://www.santostang.com/wp-login.php",
    'User-Agent':agent
}
post_data={
    'pwd':'a12345',
    'log':'test',
    'rememberme':'forever',
    'redirect_to':'http://www.santostang.com/wp-admin/',
    'testcookie':1,
}

login_page = session.post(post_url,data=post_data,headers=headers)
session.cookies = http.cookiejar.LWPCookieJar(filename='mycookies')
# session.cookies.load(ignore_discard=True)
print(login_page.status_code)
