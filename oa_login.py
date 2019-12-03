# -*- coding: utf-8 -*-
import requests, random
import time

#用户配置文件
username = "closethe"
password = "123456"
#OA配置文件
oaLoginURL0 = "http://oa.xxxxxx.com/login/Login.jsp?logintype=1"
oaLoginURL1 = "http://oa.xxxxxx.com/login/VerifyLogin.jsp"
isWorkTimeURL = "http://oa.xxxxxx.com/wui/theme/ecology8/page/getSystemTime.jsp?field=HH&token="
signURL = "http://oa.xxxxxx.com/hrm/schedule/HrmScheduleSignXMLHTTP.jsp?t="
#全局变量
user_agent_list = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53"
]
'''
signType:
1 签到
2 签退
'''
signType={
    "SignIn":"1",
    "SignOut":"2"
    }

def sign(signType = "1"):
    '''
        签到函数
        signType=="1"   签到
        signType=="2"   退出
    '''
    #获取随机的User_Agent
    UA=random.choice(user_agent_list)
    headers={'User_Agent':UA}
    s = requests.session()
    r = s.get(oaLoginURL0,headers=headers)
    #login data
    data = {
        "loginfile":"%2Fwui%2Ftheme%2Fecology8%2Fpage%2Flogin.jsp%3FtemplateId%3D3%26logintype%3D1%26gopage%3D",
        "logintype":"1",
        "fontName":"%E5%BE%AE%E8%BD%AF%E9%9B%85%E9%BB%91",
        "message":"",
        "gopage":"",
        "formmethod":"post",
        "rnd":"",
        "serial":"",
        "username":"",
        "isie":"false",
        "islanguid":"7",
        "loginid":username,
        "userpassword":password,
        "tokenAuthKey":""
    }
    r = s.post(oaLoginURL1,headers=headers,data=data)
    timeNow = int(time.time() * 1000)
    # 当前是否在工作时间
    # true (工作事件)
    testURL=isWorkTimeURL+str(timeNow)
    print testURL
    r = s.get(testURL)
    if "true" in r.text and False:
        print u"工作时间内，不可签退"
    else:
        print u"下班了"
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        signdata = {"signType":signType}
        testURL = signURL + str(random.random())
        print testURL
        r = s.post(testURL,headers=headers,data=signdata)
        print r.text


if __name__=="__main__":
    if 8 < time.localtime().tm_hour <9 :
        print "sign  in "
        #print sign(signType["SignIn"])
    elif 19 < time.localtime().tm_hour <20:
        print "sign out"
        #print sign(signType["SignOut"])
    else:
        print "not in sign time."
    
