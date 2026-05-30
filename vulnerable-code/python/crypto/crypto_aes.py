# ==============================================================
# 加密缺陷 - AES短密钥 (应被 rule14: crypto-aes-short-key 检测)
# CWE-326: Inadequate Encryption Strength
# ==============================================================

from Crypto.Cipher import AES


# --- 变体1: AES 128位密钥 (核心规则匹配) ---
def unsafe_aes_128(key, data):
    cipher = AES.new(key, key_size=128)  # 触发 rule14: AES.new($KEY, key_size=128)
    return cipher.encrypt(data)


# --- 变体2: AES ECB 模式 ---
def unsafe_aes_ecb_128(key, data):
    cipher = AES.new(key, AES.MODE_ECB, key_size=128)  # ECB + 短密钥
    return cipher.encrypt(data)


# --- 变体3: AES + 硬编码密钥 ---
def unsafe_aes_hardcoded_key(data):
    FIXED_KEY = b"16_byte_key_here"  # 16字节=128位
    cipher = AES.new(FIXED_KEY, AES.MODE_CBC, key_size=128)  # 触发 rule14
    return cipher.encrypt(data)


# --- 变体4: AES 128 CTR ---
def unsafe_aes_ctr_128(key, data):
    from Crypto.Util import Counter
    ctr = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr, key_size=128)  # 触发 rule14
    return cipher.encrypt(data)


# --- 变体5: AES + 固定IV ---
def unsafe_aes_cbc_fixed_iv_128(key, data):
    iv = b"1234567890123456"
    cipher = AES.new(key, AES.MODE_CBC, iv, key_size=128)  # 触发 rule14
    return cipher.encrypt(data)
