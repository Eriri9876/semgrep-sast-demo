# ==============================================================
# 命令注入 - os.system (应被 rule3: injection-command-os-system 检测)
# CWE-78: OS Command Injection
# ==============================================================

import os


# --- 变体1: os.system 拼接 (核心规则匹配) ---
def unsafe_os_system_concat(filename):
    os.system("ls " + filename)  # 触发 rule3: os.system("ls " + $INPUT)


# --- 变体2: os.system cat 拼接 ---
def unsafe_os_system_cat(user_file):
    os.system("cat " + user_file)  # 命令注入


# --- 变体3: os.system 多参数拼接 ---
def unsafe_os_system_multi(cmd, arg):
    os.system(cmd + " " + arg)  # 命令注入


# --- 变体4: os.system rm ---
def unsafe_os_system_rm(path):
    os.system("rm -rf " + path)  # 命令注入


# --- 变体5: os.system echo ---
def unsafe_os_system_echo(text):
    os.system("echo " + text)  # 命令注入
