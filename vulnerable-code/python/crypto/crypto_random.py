# ==============================================================
# 加密缺陷 - 不安全随机数 (应被 rule12: crypto-insecure-random 检测)
# CWE-338: Use of Cryptographically Weak PRNG
# ==============================================================

import random


# --- 变体1: random.random() (核心规则匹配) ---
def unsafe_random():
    r = random.random()  # 触发 rule12: random.random()
    return r


# --- 变体2: random.randint ---
def unsafe_randint():
    token = random.randint(100000, 999999)  # 不安全的随机令牌
    return token


# --- 变体3: random.choice ---
def unsafe_random_choice():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ''.join(random.choice(chars) for _ in range(12))  # 不安全
    return password


# --- 变体4: random.getrandbits ---
def unsafe_randbits():
    session_id = random.getrandbits(128)  # 不安全的会话ID
    return session_id


# --- 变体5: random.shuffle ---
def unsafe_shuffle_deck():
    deck = list(range(52))
    random.shuffle(deck)  # 用于加密场景时不安全
    return deck
