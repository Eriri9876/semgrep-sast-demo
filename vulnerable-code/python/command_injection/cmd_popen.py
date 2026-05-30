# ==============================================================
# 命令注入 - os.popen / eval (额外变体)
# CWE-78: OS Command Injection
# ==============================================================

import os


# --- 变体1: os.popen 读取 ---
def unsafe_popen_read(cmd):
    f = os.popen(cmd)  # 命令注入
    result = f.read()
    f.close()
    return result


# --- 变体2: os.popen 多参数 ---
def unsafe_popen_multi(prefix, suffix):
    cmd = prefix + " " + suffix
    f = os.popen(cmd)  # 命令注入
    return f.read()


# --- 变体3: eval 执行 ---
def unsafe_eval(expression):
    result = eval(expression)  # 代码注入 (Python eval)
    return result


# --- 变体4: exec 执行 ---
def unsafe_exec(code):
    exec(code)  # 代码注入 (Python exec)


# --- 变体5: __import__ ---
def unsafe_import(module_name):
    m = __import__(module_name)  # 动态导入注入
    return m
