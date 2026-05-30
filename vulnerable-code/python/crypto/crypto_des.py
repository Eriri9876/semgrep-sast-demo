# ==============================================================
# 加密缺陷 - DES加密 (应被 rule13: crypto-des-encryption 检测)
# CWE-326: Inadequate Encryption Strength
# ==============================================================

from Crypto.Cipher import DES


# --- 变体1: DES.new (核心规则匹配) ---
def unsafe_des_encrypt(key, data):
    cipher = DES.new(key)  # 触发 rule13: DES.new($KEY)
    encrypted = cipher.encrypt(data)
    return encrypted


# --- 变体2: DES3 (3DES) ---
def unsafe_3des_encrypt(key, data):
    from Crypto.Cipher import DES3
    cipher = DES3.new(key)  # 3DES 也已过时
    return cipher.encrypt(data)


# --- 变体3: DES ECB 模式 ---
def unsafe_des_ecb(key, data):
    cipher = DES.new(key, DES.MODE_ECB)  # ECB模式+DES，双重缺陷
    return cipher.encrypt(data)


# --- 变体4: DES + 固定IV ---
def unsafe_des_cbc_fixed_iv(key, data):
    iv = b"12345678"  # 固定IV
    cipher = DES.new(key, DES.MODE_CBC, iv)  # 触发 rule13
    return cipher.encrypt(data)


# --- 变体5: RC4 (另一个弱加密) ---
def unsafe_rc4(key, data):
    from Crypto.Cipher import ARC4
    cipher = ARC4.new(key)  # RC4 已不安全
    return cipher.encrypt(data)
