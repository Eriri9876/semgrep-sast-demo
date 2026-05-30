# ==============================================================
# 路径穿越 (应被 rule4: injection-path-traversal 检测)
# CWE-22: Path Traversal
# ==============================================================

import os

BASE_PATH = "/var/www/uploads/"


# --- 变体1: open 路径拼接 (核心规则匹配) ---
def unsafe_path_concat(user_file):
    f = open(BASE_PATH + user_file)  # 触发 rule4: open(BASE_PATH + $USER_FILE)
    return f.read()


# --- 变体2: 读写操作路径穿越 ---
def unsafe_path_read(user_filename):
    path = BASE_PATH + user_filename  # 触发 rule4
    with open(path, 'r') as f:
        return f.read()


# --- 变体3: 多级路径拼接 ---
APP_ROOT = "/opt/app/data/"
def unsafe_path_multi(folder, filename):
    full_path = APP_ROOT + folder + "/" + filename
    with open(full_path) as f:
        return f.read()


# --- 变体4: os.path.join + 拼接 ---
def unsafe_os_path_join(user_path):
    filepath = os.path.join(BASE_PATH, user_path) + ".txt"
    return open(filepath).read()


# --- 变体5: 文件写入路径穿越 ---
def unsafe_file_write(filename, content):
    with open(BASE_PATH + filename, 'w') as f:  # 触发 rule4
        f.write(content)
