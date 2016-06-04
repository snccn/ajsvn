#!/usr/bin/env python
# author snccn
# this is the main data node for project zjsvn
# all right now i have a url to copy from internet
# http://js.ntwikis.com/jsp/apps/cancollezh/charactors/detail.jsp?detailid=<from
# 1 to 199>
# target2:
#$.ajax({
#                url:'/rest/cancollezh/weaponsdetail',
#                type:'POST',
#                data:'detailname='+name+'&nolink=1',
#                success:function(res){

import urllib2
import urllib
import shipid


def getvaluefromPOST(url, data):

    send_headers = {'Host': 'js.ntwikis.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=send_headers)
    data = urllib.urlencode(data)
    response = urllib2.urlopen(req, data)
    raw = response.read()
    response.close()
    return raw


def getinfo(id):
    fileobj = open('data/' + str(id) + ".json", 'w')
    url = 'http://js.ntwikis.com/rest/cancollezh/charactordetail'
    data = {
        'detailid': id,
        'language': 'zh'
    }
    fileobj.write(getvaluefromPOST(url, data))
    fileobj.close()

if __name__ == '__main__':
    for i in shipid.ship_all:
        getinfo(i)
