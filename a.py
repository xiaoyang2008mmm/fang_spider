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
        b = soup1.find('div',{'class':'timu clearfix'},text=None).find('u').getText()
        c = soup1.find('a').get('href')
	print b,c

    time.sleep(1)
    i+=1







