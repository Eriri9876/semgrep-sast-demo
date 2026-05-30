# ==============================================================
# 命令注入 - subprocess (额外变体)
# CWE-78: OS Command Injection
# ==============================================================

import subprocess


# --- 变体1: subprocess.call shell=True ---
def unsafe_subprocess_call(user_input):
    subprocess.call("ping -c 1 " + user_input, shell=True)  # 命令注入


# --- 变体2: subprocess.Popen shell=True ---
def unsafe_subprocess_popen(cmd_arg):
    subprocess.Popen("grep " + cmd_arg + " /var/log/syslog", shell=True)  # 命令注入


# --- 变体3: subprocess.run shell=True ---
def unsafe_subprocess_run(filename):
    subprocess.run("cat " + filename, shell=True)  # 命令注入


# --- 变体4: subprocess.getoutput ---
def unsafe_subprocess_getoutput(user_input):
    output = subprocess.getoutput("nslookup " + user_input)  # 命令注入
    return output


# --- 变体5: subprocess.check_output ---
def unsafe_check_output(host):
    result = subprocess.check_output("host " + host, shell=True)  # 命令注入
    return result.decode()
