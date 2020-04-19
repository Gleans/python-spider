import urllib.robotparser as urobot
import requests

url = 'https://www.douban.com/robots.txt'
rp = urobot.RobotFileParser()
rp.set_url(url + "/robots.txt")
rp.read()

user_agent = 'Baiduspider'
if rp.can_fetch(user_agent, 'https://www.douban.com/product/'):
    site = requests.get(url)
    print("seems good")
else:
    print("don't post!")
