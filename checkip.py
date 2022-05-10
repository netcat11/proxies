import re
import requests
#import numpy as np
url='https://www.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f=open('66iplist.txt','r')
content=f.read()
reg=r'(\d+\.\d+\.\d+\.\d+)\s*:(\d+)'
ip_list=re.findall(reg,content)
print('total ip:'+str(len(ip_list))+'\n')
#print(ip_list)
#ip_list=np.unique(ip_list)
ip_list=set(ip_list)
print('final ip:'+str(len(ip_list)))
ok_iplist=''
for ip in ip_list:
    try:
        
        proxies={'http':ip[0]+':'+ip[1]}
        print(proxies)
        r=requests.get(url,headers=headers,proxies=proxies,timeout=1)
        print(r.status_code)
        if r.status_code==200:

            ok_iplist=ok_iplist+ip[0]+':'+ip[1]+'\n'
    except:
        continue

f=open('okip.txt','a')
f.write(ok_iplist)
f.close()
