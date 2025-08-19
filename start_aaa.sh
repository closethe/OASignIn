#!/bin/bash
# 联网认证
# web登录认证 F12 post数据里拿。
# 替换下面的userName 和 pwd值

curl 'http://1.1.1.3/ac_portal/login.php' \
  -H 'Accept: */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: http://1.1.1.3' \
  -H 'Referer: http://1.1.1.3/ac_portal/disclaimer/pc.html?template=disclaimer&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=http://1.1.1.3/homepage/index.html&controller_type=&mac=7c-7a-3c-6a-37-51' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.520.400 QQBrowser/19.2.6473.400' \
  -H 'X-Requested-With: XMLHttpRequest' \
  --data-raw 'opr=pwdLogin&userName=XXXX&pwd=XXXXXXXXXX&auth_tag=1751615283478&rememberPwd=1' \
  --compressed


curl -k https://1.1.1.3/login.html
