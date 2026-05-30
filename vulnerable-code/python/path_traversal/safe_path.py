# ==============================================================
# 安全的路径操作 (负样本 - 不应被路径穿越规则误报)
# ==============================================================

import os

BASE_PATH = "/var/www/uploads/"


# --- 安全写法1: os.path.basename ---
def safe_path_basename(user_file):
    safe_name = os.path.basename(user_file)
    with open(os.path.join(BASE_PATH, safe_name)) as f:
        return f.read()


# --- 安全写法2: realpath 验证 ---
def safe_path_realpath(user_file):
    full_path = os.path.join(BASE_PATH, user_file)
    real_path = os.path.realpath(full_path)
    if not real_path.startswith(os.path.realpath(BASE_PATH)):
        raise ValueError("Path traversal detected")
    with open(real_path) as f:
        return f.read()


# --- 安全写法3: 白名单 ---
ALLOWED_FILES = ["report.pdf", "summary.txt", "data.csv"]
def safe_path_whitelist(filename):
    if filename not in ALLOWED_FILES:
        raise ValueError("File not allowed")
    with open(os.path.join(BASE_PATH, filename)) as f:
        return f.read()


# --- 安全写法4: 去除路径分隔符 ---
def safe_path_sanitize(user_input):
    safe = user_input.replace("/", "").replace("\\", "").replace("..", "")
    return open(BASE_PATH + safe).read()
