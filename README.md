# OASignIn
泛微OA 自动签到

auto SignIn at 8:00am to 10:00am.
auto SignOut at 7:00pm to 8:00pm.

## request lib
requests

## run
```shell
# run 
python oa_login.py
```


## v1.1 新增网路认证、wireguard保护脚本、定时任务配置

```shell
# run  用于自动网路认证
start_aaa.sh
# 检测wireguard网路连通情况
check_android_wireguard.sh
# wireguard保活脚本，自动启动wireguard
start_android_wireguard.sh
```

配合cron定时任务

```shell
 t1-armbian:~:# crontab -l
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
33 * * * * /root/start_aaa.sh
*/5 * * * * /root/check_android_wireguard.sh

```
