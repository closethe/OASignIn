#!/bin/bash

# 定义要ping的IP地址
TARGET_IP="10.20.30.15"

# 定义要执行的脚本
SCRIPT_TO_RUN="./start_android_wireguard.sh"

# Ping目标IP，-c 1表示只发送一个包，-W 1表示等待1秒超时
ping -c 1 -W 1 $TARGET_IP > /dev/null 2>&1

# 检查ping命令的返回状态
if [ $? -ne 0 ]; then
    echo "Ping失败，正在执行脚本 $SCRIPT_TO_RUN ..."
    # 执行脚本
    $SCRIPT_TO_RUN
    # 检查脚本执行是否成功
    if [ $? -eq 0 ]; then
        echo "脚本执行成功"
    else
        echo "脚本执行失败"
        exit 1
    fi
else
    echo "Ping成功，无需执行脚本"
fi
