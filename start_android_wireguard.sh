#!/bin/sh

#网络认证
adb push ./start_aaa_android.sh /data/local/tmp
adb shell "chmod +x /data/local/tmp/start_aaa_android.sh "
adb shell "./data/local/tmp/start_aaa_android.sh "

#安卓启动wireguard
adb shell "am start -n com.wireguard.android/.activity.MainActivity"
