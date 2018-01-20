# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import  requests
import  json
from BeautifulSoup import BeautifulSoup
import time
from db import *


#获取区县
city_name = 'haikoushi'

url = 'http://newhouse.hn.fang.com/house/s/list/'+ city_name +'/?ctm=1.hn.xf_search.tomap.1&a=getDistAreaTag&city=hn'

quxian = (json.loads((requests.get(url)).text))['distArea']

for area in quxian:
    for k in area:
        if k == 'quanpin' and area[k] == city_name :  
	    data = area['area']
	    for c in data:
		print '区县:', c['name']

#获取均价

url2= 'http://newhouse.hn.fang.com/house/s/?ctm=1.hn.xf_search.lpsearch_area.1#no'

res2 = requests.get(url2)
res2.encoding = 'gb18030'
soups=BeautifulSoup(res2.text)
quyu_price = soups.find('li',{'class':'quyu_name bj_price'},text=None)
for k in quyu_price.findAll('a'):
    print '均价',k.getText()


#获取类型
leixings = soups.find('ul',{'id':'options_purposes'},text=None)
lxs = leixings.findAll('li',{'class':'open'},text=None)
for k in lxs:
    print '类型:', k.getText()

#获取户型
huxing = soups.findAll('a',{'data-name':'bedrooms'},text=None)

for k in huxing:
    print '户型:', k.getText()



####
mysql_data = {}

i=1
while 1:
    url = 'http://newhouse.hn.fang.com/house/s/list/'+ city_name +'/?ctm=1.hn.xf_search.tomap.1&strDistrict=%E6%B5%B7%E5%8F%A3%E5%B8%82&strSort=mobileyhnew&PageNo='+str(i)+'&zoom=12&city=hn&a=ajaxSearch'
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
	print '小区名字:',b
	print '详情页面',detail_url
	mysql_data['templet']=b
	#获取详情页的关键字	
	res = requests.get(detail_url)
	res.encoding = 'gb18030' 
	soup2=BeautifulSoup(res.text)
	#价格
	h_price = soup2.find('div',{'class':'main-info-price'},text=None)
	print '价格',h_price.getText()
	mysql_data['junjia']=h_price.getText()

	#楼盘地址
	floor_add = soup2.findAll('li',{'class':'list-text'},text=None)
	print '楼盘地址',(floor_add[1]).getText()
	mysql_data['lpdz']=(floor_add[1]).getText()

	#开发商
	dev_business = floor_add[0].getText()
	print '开发商',dev_business
	mysql_data['kfs']=dev_business	

	#项目特色
	programme = soup2.findAll('span',{'class':'tag'},text=None)
	for i in programme: print '项目特色',(i.getText())
	for i in programme: mysql_data['xmts']= (i.getText())


	#产权年限
	owner = soup2.find('div',{'class':'clearfix cqnx_512'},text=None)
	print '产权年限',owner.getText()
	mysql_data['cqnx']= owner.getText()

	#开盘时间
	sale_data = soup2.findAll('ul',{'class':'list clearfix'},text=None)
	a = (sale_data[1].findAll('div',{'class':'list-right'},text=None))[2::]
	start_time = a[0].getText() 
	print '开盘时间',start_time
	mysql_data['kpsj'] = start_time


	#获取装修状况
	d=sale_data[0].findAll('div',{'class':'list-right'},text=None)
	print '装修状况:', d[3].getText()
	mysql_data['zxzk'] = d[3].getText()

	#获取物业类别 
	print '物业类别',d[0].getText()
	mysql_data['leixing'] = d[0].getText()


	#交房时间
	rev_house_time = a[1].getText()
	print '交房时间',rev_house_time
	mysql_data['jysj'] = rev_house_time

	#售楼地址
	sale_building = a[2].getText()
	print '售楼地址',sale_building
	mysql_data['sldz'] = sale_building

	#主力户型
	mainunit = (sale_data[1].findAll('div',{'class':'list-right-text'},text=None))[0].getText() 
	print '主力户型',mainunit
	mysql_data['zlhx'] = mainunit


	######获取小区信息
	xiaoqu_info = soup2.findAll('ul',{'class':'clearfix list'},text=None)
	infos = xiaoqu_info[0].findAll('div',{'class':'list-right'},text=None)
	#物业公司
	wygs = infos[-2].getText()
	print '物业公司',wygs
	mysql_data['wygs'] = wygs	

	#建筑面积
	jsmj = infos[1].getText()
	print '建筑面积',jsmj
	mysql_data['jsmj'] = jsmj	

	#占地面积
	zdmj = infos[0].getText()
	print '占地面积',zdmj
	mysql_data['zdmj'] = zdmj

	#物业费
	wyf = infos[-1].getText()
	print '物业费',wyf
	mysql_data['wyf'] = wyf

	#绿化率
	lhl = infos[3].getText()
	print '绿化率',lhl
	mysql_data['lhl']=lhl

	#容积率
	rjl = infos[2].getText()
	print '容积率',rjl
	mysql_data['rjl'] = rjl 

	#总户数
	zhs = infos[-3].getText()	
	print '总户数',zhs
	mysql_data['zhs'] =  zhs

	#车位情况
	cwqk = infos[4].getText()	
	print '车位情况',cwqk
	mysql_data['cwqk'] =  cwqk

	#楼盘介绍
	lpjs = (soup2.find('p',{'class':'intro'},text=None)).getText() 
	print '楼盘介绍',lpjs
	mysql_data['lpjs'] = lpjs
	#配套
	pt = (soup2.find('ul',{'class':'sheshi_zb'},text=None)).getText()
	print '配套',pt
	mysql_data['pt'] = pt
	

	#获取户型图
	huxing_url = 'http://zhongyangwenhuachengld.fang.com/house/ajaxrequest/householdlist_get.php?newcode=' + str(data_id) +'&start=0&limit=100&room=all'
	huxing_data = json.loads((requests.get(huxing_url)).text)
	hx_list = []
	for k in huxing_data:
	    print '户型图:',k['houseimageurl']
	    hx_list.append(k['houseimageurl'])
	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	mysql_data['hxt'] = hx_list
	

	print  mysql_data
    time.sleep(1)
    i+=1
	
    #插入数据
    #DedeAddon1718.create(**mysql_data)







