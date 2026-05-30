# ==============================================================
# 安全的认证写法 (负样本 - 不应被认证相关规则误报)
# ==============================================================

import hashlib
import requests
import os


# --- 安全写法1: 使用 bcrypt ---
def safe_hash_bcrypt(password):
    import bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


# --- 安全写法2: 使用 SHA256 + 随机盐 ---
def safe_hash_sha256(password):
    salt = os.urandom(32)
    h = hashlib.sha256(salt + password.encode())
    return salt.hex() + ":" + h.hexdigest()


# --- 安全写法3: HTTPS 请求 ---
def safe_https_request(url):
    resp = requests.get("https://" + url)  # 使用 HTTPS
    return resp.json()


# --- 安全写法4: SSL证书验证 ---
def safe_ssl_verify(url):
    resp = requests.get("https://" + url, verify=True)  # 启用SSL验证
    return resp.text


# --- 安全写法5: 使用环境变量存储密码 ---
def safe_login(username):
    from passlib.hash import argon2
    stored_hash = os.environ.get("PASSWORD_HASH")
    return argon2.verify(username, stored_hash)
