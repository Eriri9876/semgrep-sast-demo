# ==============================================================
# 调试信息泄露 (应被 rule20: general-debug-info-leak 检测)
# CWE-489: Active Debug Code
# ==============================================================

import os


# --- 变体1: print DEBUG (核心规则匹配) ---
def debug_leak_print(user_data):
    print("DEBUG:", user_data)  # 触发 rule20: print("DEBUG:", $DATA)


# --- 变体2: 多处调试输出 ---
def debug_multi(data):
    print("DEBUG: request body =", data)  # 触发 rule20
    print("DEBUG: headers =", data)  # 触发 rule20


# --- 变体3: 敏感信息日志 ---
def debug_sensitive(password, token):
    print("DEBUG: password =", password)  # 触发 rule20 + 敏感数据泄露
    print("DEBUG: access_token =", token)  # 触发 rule20


# --- 变体4: 异常堆栈泄露 ---
def debug_exception():
    import traceback
    try:
        raise ValueError("test")
    except Exception as e:
        print("DEBUG:", traceback.format_exc())  # 触发 rule20


# --- 变体5: 环境变量打印 ---
def debug_env():
    print("DEBUG: env vars =", os.environ)  # 触发 rule20 + 极度危险
