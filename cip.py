import re
import random
def getrandomip():
    f=open('ipl.txt','r')
    content=f.read()
    reg=r'(\d+\.\d+\.\d+\.\d+)\s*:(\d+)'
    ip_list=re.findall(reg,content)
    random_ip=random.choice(ip_list)
    proxies={'http':random_ip[0]+':'+random_ip[1]}
    return proxies
