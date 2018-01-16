# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import  requests
import  json
from BeautifulSoup import BeautifulSoup
import time



i=1
while 1:
    url = 'http://newhouse.hn.fang.com/house/s/list/haikoushi/?ctm=1.hn.xf_search.tomap.1&strDistrict=%E6%B5%B7%E5%8F%A3%E5%B8%82&strSort=mobileyhnew&PageNo='+str(i)+'&zoom=12&city=hn&a=ajaxSearch'
    r = requests.get(url)
    data = json.loads(r.text)
    if data['data'] == "false" :   break
    houses = data['list']
    soup=BeautifulSoup(''.join(houses))           
    a=soup.findAll('li',{'class':'clearfix'},text=None)
    for url in a:
        soup1=BeautifulSoup(''.join(str(url)))
	data_id= soup1.find('li').get('data-id')
        b = soup1.find('div',{'class':'timu clearfix'},text=None).find('u').getText()
        c = soup1.find('a').get('href')
	detail_url = c + '/house/'+ str(data_id) +'/housedetail.htm' 
	print '#########'
	print b, detail_url
	#获取详情页的关键字	
	res = requests.get(detail_url)
	res.encoding = 'gb18030' 
	soup2=BeautifulSoup(res.text)
	#价格
	h_price = soup2.find('div',{'class':'main-info-price'},text=None)
	print h_price.getText()
	#楼盘地址
	floor_add = soup2.findAll('li',{'class':'list-text'},text=None)
	print (floor_add[1]).getText()
	#开发商
	dev_business = floor_add[0].getText()
	print dev_business
	#项目特色
	programme = soup2.findAll('span',{'class':'tag'},text=None)
	for i in programme: print (i.getText())
	#产权年限
	owner = soup2.find('div',{'class':'clearfix cqnx_512'},text=None)
	print owner.getText()
	#开盘时间


	

    time.sleep(1)
    i+=1







