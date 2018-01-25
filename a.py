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

"""
quxian = (json.loads((requests.get(url)).text))['distArea']

for area in quxian:
    for k in area:
        if k == 'quanpin' and area[k] == city_name :  
	    data = area['area']
	    for c in data:
		#print '区县:', c['name']

#获取均价

url2= 'http://newhouse.hn.fang.com/house/s/?ctm=1.hn.xf_search.lpsearch_area.1#no'

res2 = requests.get(url2)
res2.encoding = 'gb18030'
soups=BeautifulSoup(res2.text)
quyu_price = soups.find('li',{'class':'quyu_name bj_price'},text=None)
for k in quyu_price.findAll('a'):
    #print '均价',k.getText()


#获取类型
leixings = soups.find('ul',{'id':'options_purposes'},text=None)
lxs = leixings.findAll('li',{'class':'open'},text=None)
for k in lxs:
    #print '类型:', k.getText()

#获取户型
huxing = soups.findAll('a',{'data-name':'bedrooms'},text=None)

for k in huxing:
    #print '户型:', k.getText()


"""

####

page=1
j=1   #循坏计数MySQL的id
while 1:
    url = 'http://newhouse.hn.fang.com/house/s/list/'+ city_name +'/?ctm=1.hn.xf_search.tomap.1&strDistrict=%E6%B5%B7%E5%8F%A3%E5%B8%82&strSort=mobileyhnew&PageNo='+str(page)+'&zoom=12&city=hn&a=ajaxSearch'
    r = requests.get(url)
    data = json.loads(r.text)
    if data['data'] == "false" :   break
    houses = data['list']
    soup=BeautifulSoup(''.join(houses))           
    a=soup.findAll('li',{'class':'clearfix'},text=None)
    for url in a:
	mysql_data = {}
        soup1=BeautifulSoup(''.join(str(url)))
	data_id= soup1.find('li').get('data-id')
        b = soup1.find('div',{'class':'timu clearfix'},text=None).find('u').getText()
        c = soup1.find('a').get('href')
	detail_url = c + '/house/'+ str(data_id) +'/housedetail.htm' 
	#print '小区名字:',b
	#print '详情页面',detail_url
	try:
	    #mysql_data['templet']=b
	    pass
	except:
	    pass
	#获取详情页的关键字	
	res = requests.get(detail_url)
	res.encoding = 'gb18030' 
	soup2=BeautifulSoup(res.text)
	#价格
	h_price = soup2.find('div',{'class':'main-info-price'},text=None)
	#print '价格',h_price.getText()
	try:
	    mysql_data['junjia']=((h_price.getText()).split('：'))[1]
	except:
	    pass

	#楼盘地址
	floor_add = soup2.findAll('li',{'class':'list-text'},text=None)
	#print '楼盘地址',(floor_add[1]).getText()
	try:
	    mysql_data['lpdz']=((floor_add[1]).getText()).split('：')[1]
        except:
            pass

	#开发商
	try:
	    dev_business = floor_add[0].getText()
	except:
	    pass
	#print '开发商',dev_business
	try:
	    if '开发商' in dev_business:
		dev_business = dev_business.split('：')[1]
	    mysql_data['kfs']=dev_business	
        except:
            pass

	#项目特色
	programme = soup2.findAll('span',{'class':'tag'},text=None)
	#for i in programme: #print '项目特色',(i.getText())
	try:
	    for i in programme: mysql_data['xmts']= (i.getText())
        except:
            pass


	#产权年限
	owner = soup2.find('div',{'class':'clearfix cqnx_512'},text=None)
	#print '产权年限',owner.getText()
	try:
	    mysql_data['cqnx']= owner.getText()
        except:
            pass

	#开盘时间
	sale_data = soup2.findAll('ul',{'class':'list clearfix'},text=None)
	try:
	    a = (sale_data[1].findAll('div',{'class':'list-right'},text=None))[2::]
	    start_time = a[0].getText() 
	except:
	    pass

	#print '开盘时间',start_time
	try:
	    mysql_data['kpsj'] = (start_time.split('['))[0]
        except:
            pass


	#获取装修状况
	try:
	    d=sale_data[0].findAll('div',{'class':'list-right'},text=None)
	except:
	    pass
	#print '装修状况:', d[3].getText()
	try:
	    mysql_data['zxzk'] = d[3].getText()
        except:
            pass

	#获取物业类别 
	#print '物业类别',d[0].getText()
	try:
	    mysql_data['leixing'] = d[0].getText()
        except:
            pass


	#交房时间
	rev_house_time = a[1].getText()
	#print '交房时间',rev_house_time
	try:
	    if  '[交房时间详情1]' in rev_house_time:
		rev_house_time = rev_house_time.split('[')[0]
	    mysql_data['jysj'] = rev_house_time
        except:
            pass

	#售楼地址
	sale_building = a[2].getText()
	#print '售楼地址',sale_building
	try:
	    mysql_data['sldz'] = sale_building
        except:
            pass

	#主力户型
	try:
	    mainunit = (sale_data[1].findAll('div',{'class':'list-right-text'},text=None))[0].getText() 
	except:
	    pass
	#print '主力户型',mainunit
	try:
	    
	    zlhx = mainunit
	    rep=re.sub('\(\d+\)',',',zlhx)
	    mysql_data['zlhx'] = rep
        except:
            pass


	######获取小区信息
	try:
	    xiaoqu_info = soup2.findAll('ul',{'class':'clearfix list'},text=None)
	    infos = xiaoqu_info[0].findAll('div',{'class':'list-right'},text=None)
	    #物业公司
	    wygs = infos[-2].getText()
	except:
	    pass
	#print '物业公司',wygs
	try:
	    mysql_data['wygs'] = wygs	
        except:
            pass

	#建筑面积
	jsmj = infos[1].getText()
	#print '建筑面积',jsmj
	try:
	    mysql_data['jsmj'] = jsmj	
        except:
            pass

	#占地面积
	zdmj = infos[0].getText()
	#print '占地面积',zdmj
	try:
	    mysql_data['zdmj'] = zdmj
        except:
            pass

	#物业费
	wyf = infos[-1].getText()
	#print '物业费',wyf
	try:	
	    mysql_data['wyf'] = wyf
        except:
            pass

	#绿化率
	lhl = infos[3].getText()
	#print '绿化率',lhl
	try:
	    mysql_data['lhl']=lhl
        except:
            pass

	#容积率
	rjl = infos[2].getText()
	#print '容积率',rjl
	try:
	    mysql_data['rjl'] = rjl 
        except:
            pass

	#总户数
	zhs = infos[-3].getText()	
	#print '总户数',zhs
	try:
	    mysql_data['zhs'] =  zhs
        except:
            pass

	#车位情况
	cwqk = infos[4].getText()	
	#print '车位情况',cwqk
	try:
	    mysql_data['cwqk'] =  cwqk
        except:
            pass

	#楼盘介绍
	try:
	    lpjs = (soup2.find('p',{'class':'intro'},text=None)).getText() 
	except:
	    pass
	#print '楼盘介绍',lpjs
	try:
	    mysql_data['lpjs'] = lpjs
        except:
            pass
	#配套
	try:
	    pt = (soup2.find('ul',{'class':'sheshi_zb'},text=None)).getText()
	except:
	    pass
	#print '配套',pt
	try:
	    mysql_data['pt'] = pt
        except:
            pass
	

	#获取户型图
	huxing_url = 'http://zhongyangwenhuachengld.fang.com/house/ajaxrequest/householdlist_get.php?newcode=' + str(data_id) +'&start=0&limit=100&room=all'
	huxing_data = json.loads((requests.get(huxing_url)).text)
	hx_str = ''
	for k in huxing_data:
	    #print '户型图:',k['houseimageurl']
	    tupian_name = '_'.join((k['houseimageurl']).split('/')[-2:])
	    hx_str= hx_str +'<img alt="" src="/uploads/allimg/fangtianxia/' + tupian_name  +'" style="width: 220px; height: 146px;" />'+ ' '
	try:
	     mysql_data['hxt'] = hx_str
	except:
            pass
	

	##自定义增加类型字段
	mysql_data['typeid'] = 8
	mysql_data['aid'] = j

	print  mysql_data
    	#插入数据
    	DedeAddon21.create(**mysql_data)


	#表DedeArchives
	archive_dict = {}
	archive_dict['id']=j
        archive_dict['typeid']=8 
        archive_dict['typeid2']=0
        archive_dict['sortrank']=1514189805 
        archive_dict['flag']= 'p'
        archive_dict['ismake'] = 1
        archive_dict['channel']=  21
        archive_dict['arcrank']=  0
        archive_dict['click']=  33
        archive_dict['money']=  0
        archive_dict['title']=  b
        archive_dict['shorttitle']= '' 
        archive_dict['color']=  ''
        archive_dict['writer']=  'admin'
        archive_dict['source']=  ''
        archive_dict['litpic']= '/img'
        archive_dict['pubdate']= 1514189805 
        archive_dict['senddate']=  1514189805
        archive_dict['mid']= 1
        archive_dict['keywords']= '关键词'
        archive_dict['lastpost']= 0
        archive_dict['scores']= 0
        archive_dict['goodpost']=0 
        archive_dict['badpost']= 0
        archive_dict['voteid']= 0
        archive_dict['notpost']= 0
        archive_dict['description']= '描述'
        archive_dict['filename']= ''
        archive_dict['dutyadmin']= 1
        archive_dict['tackid']= 0
        archive_dict['mtype']= 0
        archive_dict['weight']= 25
	
	DedeArchives.create(**archive_dict)


	#表 dede_arctiny
	arctiny_dict={}
        arctiny_dict['id'] = j 
        arctiny_dict['typeid'] = 8   
        arctiny_dict['typeid2'] = 0 
        arctiny_dict['arcrank'] = 0
        arctiny_dict['channel'] = 21
        arctiny_dict['senddate'] = 1514189805 
        arctiny_dict['sortrank'] =  1514189805
        arctiny_dict['mid'] =  1

	DedeArctiny.create(**arctiny_dict)

    	j+=1

	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    time.sleep(1)
    page=page+1
	







