# ==============================================================
# 认证缺陷 - 弱哈希算法 (应被 rule10: auth-weak-hash-md5 检测)
# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
# ==============================================================

import hashlib


# --- 变体1: hashlib.md5 (核心规则匹配) ---
def unsafe_hash_md5(password):
    h = hashlib.md5(password)  # 触发 rule10: hashlib.md5($DATA)
    return h.hexdigest()


# --- 变体2: MD5 直接调用 ---
def verify_md5_hash(user_input, stored_hash):
    input_hash = hashlib.md5(user_input.encode()).hexdigest()  # 触发 rule10
    return input_hash == stored_hash


# --- 变体3: SHA1 ---
def unsafe_hash_sha1(data):
    h = hashlib.sha1(data)  # SHA1 也已被攻破
    return h.hexdigest()


# --- 变体4: 双重MD5 ---
def unsafe_double_md5(password):
    h1 = hashlib.md5(password)  # 触发 rule10
    h2 = hashlib.md5(h1.hexdigest().encode())  # 触发 rule10
    return h2.hexdigest()


# --- 变体5: MD5 + 固定盐 ---
def unsafe_md5_salt(password):
    salt = "my_fixed_salt"
    h = hashlib.md5((password + salt).encode())  # 触发 rule10
    return h.hexdigest()
