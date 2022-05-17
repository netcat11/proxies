import re
import requests
import time
import cip
ipl=''
regkdl=r'<td data-title="IP">(\d+\.\d+\.\d+\.\d+)</td>\s*<td data-title="PORT">(\d+)</td>'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
reg66ip=r'<td>(\d+\.\d+\.\d+\.\d+)</td><td>(\d+)</td>'
def getip(url,reg):
 global ipl
 try:
     
  r=requests.get(url,headers=headers,proxies=cip.getrandomip(),timeout=2)
  if r.status_code==200:

   print(r.status_code)
   ip_list=re.findall(reg,r.text)
   ip_list=set(ip_list)
   print(ip_list)
 
   for ip in ip_list:
     
     if ip[0] in ipl:
         continue
     else:   
      ipl=ipl+ip[0]+':'+ip[1]+'\n'
  else:
      print(r.status_code)
      getip(url,reg)
 except:
     print('ip封禁，获取页面失败！.....')
     getip(url,reg)
   
     
def kdl(p):
 for i in range(1,p):
    global regkdl 
    url='https://www.kuaidaili.com/free/inha/'+str(i)+'/'
    print("正在爬取第:"+str(i)+'页')
    getip(url,regkdl)
    time.sleep(2)

 f=open('ip.txt','a')
 f.write(ipl)
 f.close()

def g66ip(p):
 for i in range(1,p):
    print("正在爬取第:"+str(i)+'页')
    url='http://www.66ip.cn/'+str(i)+'.html'
    getip(url,reg66ip)
 f=open('66iplist.txt','a')
 f.write(ipl)
 f.close()
