# ==============================================================
# 安全的命令执行写法 (负样本 - 不应被命令注入规则误报)
# ==============================================================

import subprocess
import os


# --- 安全写法1: subprocess 使用列表参数 ---
def safe_subprocess_list(host):
    # 使用列表传参，不经过 shell
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
    return result.stdout


# --- 安全写法2: shell=False (默认) ---
def safe_subprocess_no_shell(filename):
    subprocess.run(["cat", filename], capture_output=True)  # shell=False 是默认值


# --- 安全写法3: 白名单验证 ---
def safe_whitelist_command(action):
    ALLOWED_ACTIONS = ["status", "start", "stop"]
    if action not in ALLOWED_ACTIONS:
        raise ValueError("Invalid action")
    os.system("systemctl " + action + " nginx")  # 经过白名单验证


# --- 安全写法4: shlex.quote 转义 ---
def safe_shlex_quote(user_input):
    import shlex
    safe_arg = shlex.quote(user_input)
    subprocess.run(["echo", safe_arg])


# --- 安全写法5: 使用函数而非命令 ---
def safe_no_command(filename):
    # 直接用Python文件操作而非shell命令
    with open(filename, 'r') as f:
        content = f.read()
    return content
