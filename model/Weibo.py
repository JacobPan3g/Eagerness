# coding=utf8
'''
Created on May 20, 2013

@author: jacob
'''

from weibo import APIClient
from re import split
import re
import urllib,httplib
import webbrowser
from urllib import urlretrieve
import codecs
import os
import pickle


APP_KEY = "861058711"
APP_SECRET = "242b3fc47e1833dd62528ebaef4573de"
#APP_KEY = "1419571836"
#APP_SECRET = "2cac5bf9d6294ebaff56ca8dc6f323f7"
CALLBACK_URL = "http://api.weibo.com/oauth2/default.html"
ACCOUNT = "zhenjian3g@qq.com"#帐号
PASSWORD = "jacobpan2889184"#密码

dealWithData = {"zip","pdf","rar","doc",u"共享资源下载",u"抱歉,此微博已被作者删除。查看",u"抱歉,此微博已被删除。如需帮助,请私信给",u"转发",u"分享",u"微刊",u"详情",u"微博",u"下载",u"帮助",u"私信","Repost","mark","Mark","by","via",u"- 共享资料", u"（转）"}

def authentication( usr, pwd ):
    
    user_info_file = 'cur/%s.info' % usr;
    user_weibos_file = "cur/" + usr + '.weibos'
    if os.path.exists(user_info_file) and os.path.exists(user_weibos_file):
        userInfo, allstatus = loadUserSession( user_info_file, user_weibos_file )      
    else: 
        #get url
        client = APIClient(app_key = APP_KEY,app_secret = APP_SECRET,redirect_uri=CALLBACK_URL)
        url = client.get_authorize_url()
    
        #get code
        conn = httplib.HTTPSConnection('api.weibo.com')
        postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':usr,'passwd':pwd,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
        conn.request('POST','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'})
        res = conn.getresponse()
        location = res.getheader('location')
        #print location
        code = location.split('=')[1]
        conn.close()

        #get client        
        r = client.request_access_token(code)
        #print r.uid
        access_token = r.access_token 
        expires_in = r.expires_in 
        client.set_access_token(access_token, expires_in)
    
        #name=u"振坚_Jacob"
        #print name
        #alltext = client.statuses__user_timeline(screen_name=name,count=100,page=i)
        #print alltext
    
        uid = r.uid
        allstatus = getAllstatus( user_weibos_file, client, uid )
        #allstatus be saved
        #print allstatus
    
        userInfo = getUserInfo( client, uid )
        saveUserInfo( userInfo, user_info_file )
    
    return userInfo, allstatus

    
def getUserInfo( client, uid ):
    info_d = dict( client.users__show( uid=uid ) )
    userInfo = dict()
    userInfo["uid"] = uid
    userInfo["name"] = info_d["screen_name"]
    userInfo["image"] = info_d["avatar_large"]
    userInfo["description"] = info_d["description"]
    print userInfo
    return userInfo
    
def getAllstatus( user_weibos_file, client, uid ):
    i = 1
    try:
        data = codecs.open(user_weibos_file, 'w', "utf8")
        while i <= 20:
            #use API to get data
            alltext = client.statuses__user_timeline(uid=uid,count=100,page=i)
            i=i+1
            d=dict(alltext)
            if (len(d['statuses']) == 0) :
                break;
            for j in range(len(d['statuses'])):
                try:
                    (str1,str2) = d['statuses'][j]['text'].split('//',1)
                except:
                    str1 = d['statuses'][j]['text']
                str1 = deal_with_data(str1)

                if not str1 == "":
                    data.write(str1)
                    data.write("\n")
                try:
                    str2 = d['statuses'][j]['retweeted_status']['text']
                    str2 = dealWithData(str2)
                    if not str2 == "":
                        data.write(str2)
                        data.write("\n")
                except:
                    pass
    except IOError as err:
        print err
        pass
    finally:
        data.close()
        fobj = open( user_weibos_file )
        allstatus = fobj.read()
        fobj.close()
        return allstatus
        

def deal_with_data(string):
    pattern = re.compile('@[^\s]*')
    pattern1 = re.compile('http[^\s]*')
    pattern2 = re.compile('\[[^\s]*\]')
    pattern3 = re.compile('[0-9]*')
    pattern4 = re.compile('www[^\s]*')

    result = re.split(pattern,string)
    string = "".join(result)
    result = re.split(pattern1,string)
    string = "".join(result)
    result = re.split(pattern2,string)
    string = "".join(result)
    result = re.split(pattern3,string)
    string = "".join(result)
    result = re.split(pattern4,string)
    string = "".join(result)
    for tmp in dealWithData:
        string = string.replace(tmp,'')
    string = string.replace('.',' ')
    return string

def saveUserInfo( userInfo, user_info_file ):
    fobj = open( user_info_file, 'wb' )
    pickle.dump( userInfo, fobj )
    fobj.close()

def loadUserSession( user_info_file, user_weibos_file ):
    fobj = open( user_info_file, 'rb' )
    userInfo = pickle.load( fobj )
    fobj.close()
    fobj = open( user_weibos_file )
    allstatus = fobj.read()
    fobj.close()
    return userInfo, allstatus

# For model testing
if __name__ == '__main__':
    authentication( ACCOUNT, PASSWORD )
    
