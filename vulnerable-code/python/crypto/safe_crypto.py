# ==============================================================
# 安全的加密写法 (负样本 - 不应被加密规则误报)
# ==============================================================

import os
from Crypto.Cipher import AES


# --- 安全写法1: AES 256位密钥 ---
def safe_aes_256(key, data):
    # key应至少32字节=256位
    cipher = AES.new(key, AES.MODE_GCM)  # 使用GCM模式
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return ciphertext, tag, cipher.nonce


# --- 安全写法2: 安全随机数 ---
def safe_random_token():
    token = os.urandom(32)  # 加密安全的随机数
    return token.hex()


# --- 安全写法3: secrets 模块 ---
def safe_secrets_token():
    import secrets
    return secrets.token_urlsafe(32)  # Python 3.6+


# --- 安全写法4: ChaCha20 ---
def safe_chacha20(key, data):
    from Crypto.Cipher import ChaCha20
    cipher = ChaCha20.new(key=key)
    return cipher.encrypt(data)


# --- 安全写法5: 密钥派生 ---
def safe_key_derivation(password, salt):
    from Crypto.Protocol.KDF import PBKDF2
    key = PBKDF2(password, salt, dkLen=32, count=100000)  # 256位密钥
    return key
