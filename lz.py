import xlrd
from xlutils.copy import copy
import ocr
import os, sys
import re
c_folder='./2222'
dirs=os.listdir(c_folder)
r=2
def insert_data(r,result,bins,weight,price,contract,country):
 readbook=xlrd.open_workbook('2021.xls')
 wb=copy(readbook)
 sh1=wb.get_sheet(0)
 sh1.write(r,1,result['words_result'][0]['words'])# time
 sh1.write(r,2,bins)#  bins
 sh1.write(r,3,weight)# weight
 #sh1.write(r,4,int(price)/int(weight)) #unit price
 sh1.write(r,5,price)#price
 sh1.write(r,6,contract) #contract
 sh1.write(r,7,result['words_result'][2]['words']) # r of inspection
 sh1.write(r,8,country) #eport country
 wb.save('2021.xls')


""" 
def identify(it):
    if it in dir():
       pass
    else:
            globals()[it]='识别错误'
             """
def p_getd(result,r):
    bins,weight,price,contract,country='','','','',''
    for i in range(0,60):
        item=result['words_result'][i]['words']
    #for item in result['words_result']:
     #   item=item['words']
        if '双瓦楞纸箱' in item:
            bins=item[6:]
        elif '上饶市婺源县' in item:
            #weight=item[6:-2]
            if item:
             weight=re.findall('\d+',item)

        elif '美元' in item:
            #price=item[:-2]
            if item:
             price= re.findall('\d+',item)[0]
        elif 'LZ' in item:
            contract=item
        elif item in '俄罗斯马来西亚哈萨克斯坦中国香港':
            country=item

    insert_data(r,result,bins,weight,price,contract,country)
    
for file in dirs:
    file=c_folder+'/'+file
    image=ocr.get_img(file)
    result=ocr.client.basicGeneral(image)
    #insert_data(r,result)
    r=r+1
    print('正在打印第'+str(r-2)+'页')
    p_getd(result,r)

    

